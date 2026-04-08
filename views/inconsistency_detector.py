"""Inconsistency Detector View — automatically flag analyst disagreements."""

import streamlit as st
import pandas as pd
import numpy as np

from components.charts import agreement_heatmap
from components.tables import inconsistency_table


def _detect_inconsistencies(forecasts_df: pd.DataFrame, reports_df: pd.DataFrame) -> list[dict]:
    """Analyze forecasts and reports to find inconsistencies."""
    issues = []

    # --- 1. High-spread metrics (CV > 30%) ---
    for metric in forecasts_df["Metric"].unique():
        metric_data = forecasts_df[forecasts_df["Metric"] == metric]
        metric_data = metric_data[metric_data["Year"] <= 2031]

        for year in metric_data["Year"].unique():
            year_data = metric_data[metric_data["Year"] == year]
            if len(year_data) < 3:
                continue

            mean_val = year_data["Value"].mean()
            std_val = year_data["Value"].std()
            if mean_val == 0:
                continue

            cv = abs(std_val / mean_val) * 100
            spread_pct = (year_data["Value"].max() - year_data["Value"].min()) / abs(mean_val) * 100

            if cv > 35:
                high = year_data.loc[year_data["Value"].idxmax()]
                low = year_data.loc[year_data["Value"].idxmin()]
                unit = year_data["Unit"].iloc[0]
                issues.append({
                    "Type": "High Disagreement",
                    "Metric": metric,
                    "Year": f"{int(year)}E",
                    "Severity": "High" if cv > 50 else "Medium",
                    "Details": (
                        f"CV={cv:.0f}%. {high['Publisher']} ({high['Value']:,.0f}{unit}) vs. "
                        f"{low['Publisher']} ({low['Value']:,.0f}{unit}). "
                        f"Spread: {spread_pct:.0f}% of mean."
                    ),
                })

    # --- 2. Rating contradictions ---
    if not reports_df.empty:
        bullish = {"Overweight", "Buy", "Outperform"}
        bearish = {"Underweight", "Sell", "Underperform"}
        neutral = {"Neutral", "Equal Weight", "Hold"}

        ratings = reports_df[["Publisher", "Rating", "Price Target"]].copy()
        has_bullish = any(r in bullish for r in ratings["Rating"])
        has_bearish = any(r in bearish for r in ratings["Rating"])
        has_neutral = any(r in neutral for r in ratings["Rating"])

        # Check for wide PT dispersion with opposing ratings
        pt_max = ratings["Price Target"].max()
        pt_min = ratings["Price Target"].min()
        pt_spread = (pt_max - pt_min) / ratings["Price Target"].median() * 100

        if pt_spread > 50:
            high_pub = ratings.loc[ratings["Price Target"].idxmax()]
            low_pub = ratings.loc[ratings["Price Target"].idxmin()]
            issues.append({
                "Type": "Price Target Dispersion",
                "Metric": "Price Target",
                "Year": "Current",
                "Severity": "High",
                "Details": (
                    f"${pt_max:.0f} ({high_pub['Publisher']}, {high_pub['Rating']}) vs. "
                    f"${pt_min:.0f} ({low_pub['Publisher']}, {low_pub['Rating']}). "
                    f"Spread: {pt_spread:.0f}% of median."
                ),
            })

        if has_bullish and has_neutral and pt_spread > 30:
            issues.append({
                "Type": "Rating Divergence",
                "Metric": "Rating",
                "Year": "Current",
                "Severity": "Medium",
                "Details": (
                    "Analysts have diverging views — some rate Buy/Overweight while others are "
                    "at Neutral/Hold. Key debate: competitive risk and peak sales potential."
                ),
            })

    # --- 3. Launch timeline disagreements ---
    launch_data = forecasts_df[forecasts_df["Metric"] == "Schizophrenia Launch Year"]
    if not launch_data.empty:
        launch_years = launch_data["Value"].unique()
        if len(set(launch_years)) > 1:
            early = launch_data.loc[launch_data["Value"].idxmin()]
            late = launch_data.loc[launch_data["Value"].idxmax()]
            gap = int(late["Value"] - early["Value"])
            issues.append({
                "Type": "Timeline Conflict",
                "Metric": "Schizophrenia Launch Year",
                "Year": "—",
                "Severity": "High" if gap >= 2 else "Medium",
                "Details": (
                    f"{early['Publisher']} expects launch in {int(early['Value'])} vs. "
                    f"{late['Publisher']} in {int(late['Value'])}. "
                    f"{gap}-year gap in expected launch timelines."
                ),
            })

    # --- 4. PoS estimate disagreement ---
    pos_data = forecasts_df[forecasts_df["Metric"] == "Schizophrenia Phase 3 PoS"]
    if len(pos_data) >= 3:
        pos_spread = pos_data["Value"].max() - pos_data["Value"].min()
        if pos_spread > 20:
            high = pos_data.loc[pos_data["Value"].idxmax()]
            low = pos_data.loc[pos_data["Value"].idxmin()]
            issues.append({
                "Type": "PoS Disagreement",
                "Metric": "Schizophrenia Phase 3 PoS",
                "Year": "—",
                "Severity": "High" if pos_spread > 25 else "Medium",
                "Details": (
                    f"{high['Publisher']} assigns {high['Value']:.0f}% PoS vs. "
                    f"{low['Publisher']} at {low['Value']:.0f}%. "
                    f"{pos_spread:.0f}pp spread in probability estimates."
                ),
            })

    # --- 5. Peak sales disagreement ---
    for metric in ["Schizophrenia Revenue", "MDD Revenue"]:
        peak_data = forecasts_df[(forecasts_df["Metric"] == metric) & (forecasts_df["Year"] > 2031)]
        if len(peak_data) >= 3:
            ratio = peak_data["Value"].max() / peak_data["Value"].min() if peak_data["Value"].min() > 0 else 0
            if ratio > 2:
                high = peak_data.loc[peak_data["Value"].idxmax()]
                low = peak_data.loc[peak_data["Value"].idxmin()]
                issues.append({
                    "Type": "Peak Sales Divergence",
                    "Metric": f"{metric} (Peak)",
                    "Year": "Peak",
                    "Severity": "High",
                    "Details": (
                        f"{high['Publisher']} models ${high['Value']:,.0f}M peak vs. "
                        f"{low['Publisher']} at ${low['Value']:,.0f}M. "
                        f"Bull/bear ratio: {ratio:.1f}x."
                    ),
                })

    return sorted(issues, key=lambda x: {"High": 0, "Medium": 1, "Low": 2}.get(x["Severity"], 3))


def render(forecasts_df: pd.DataFrame, reports_df: pd.DataFrame):
    """Render the Inconsistency Detector view."""

    st.header("Inconsistency Detector")
    st.caption("Automatically flags where analysts disagree — contradicting assumptions, outlier forecasts, and divergent timelines.")

    # --- Summary metrics ---
    inconsistencies = _detect_inconsistencies(forecasts_df, reports_df)

    high_count = sum(1 for i in inconsistencies if i["Severity"] == "High")
    medium_count = sum(1 for i in inconsistencies if i["Severity"] == "Medium")
    low_count = sum(1 for i in inconsistencies if i["Severity"] == "Low")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Issues", len(inconsistencies))
    with col2:
        st.metric("🔴 High", high_count)
    with col3:
        st.metric("🟡 Medium", medium_count)
    with col4:
        st.metric("🟢 Low", low_count)

    st.divider()

    # --- Heatmap ---
    st.markdown("#### Analyst Agreement Heatmap")
    st.caption("Higher values (red) = more disagreement. Green = consensus.")

    key_metrics = ["Schizophrenia Revenue", "MDD Revenue", "Total Revenue", "EPS"]
    fig = agreement_heatmap(forecasts_df, metrics=key_metrics)
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # --- Inconsistency list ---
    st.markdown("#### Flagged Inconsistencies")

    # Filter by type
    issue_types = sorted(set(i["Type"] for i in inconsistencies))
    selected_types = st.multiselect("Filter by type", issue_types, default=issue_types,
                                      key="inconsistency_type_filter")

    filtered = [i for i in inconsistencies if i["Type"] in selected_types]
    inconsistency_table(filtered)

    # --- Detailed breakdown by type ---
    st.divider()
    st.markdown("#### Key Debates")

    # Price target range
    pt_data = forecasts_df[forecasts_df["Metric"] == "Price Target"]
    if not pt_data.empty:
        with st.expander("💰 Price Target Range", expanded=True):
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("**Bull Case**")
                bull = pt_data.loc[pt_data["Value"].idxmax()]
                bull_report = reports_df[reports_df["Publisher"] == bull["Publisher"]].iloc[0]
                st.markdown(f"**{bull['Publisher']}** — ${bull['Value']:.0f}")
                st.markdown(f"Rating: {bull_report['Rating']}")
                st.markdown(f"*{bull_report['Key Themes'][0]}*")
            with col_b:
                st.markdown("**Bear Case**")
                bear = pt_data.loc[pt_data["Value"].idxmin()]
                bear_report = reports_df[reports_df["Publisher"] == bear["Publisher"]].iloc[0]
                st.markdown(f"**{bear['Publisher']}** — ${bear['Value']:.0f}")
                st.markdown(f"Rating: {bear_report['Rating']}")
                st.markdown(f"*{bear_report['Key Themes'][0]}*")

    # Peak sales debate
    peak_schiz = forecasts_df[(forecasts_df["Metric"] == "Schizophrenia Revenue") &
                               (forecasts_df["Year"] > 2031)]
    if not peak_schiz.empty:
        with st.expander("💊 Schizophrenia Peak Sales Debate", expanded=True):
            for _, row in peak_schiz.sort_values("Value", ascending=False).iterrows():
                bar_pct = row["Value"] / peak_schiz["Value"].max() * 100
                pub_report = reports_df[reports_df["Publisher"] == row["Publisher"]]
                rating = pub_report.iloc[0]["Rating"] if not pub_report.empty else "N/A"
                st.markdown(f"**{row['Publisher']}** ({rating}): **${row['Value']:,.0f}M**")
                st.progress(bar_pct / 100)

    # Launch timeline
    launch = forecasts_df[forecasts_df["Metric"] == "Schizophrenia Launch Year"]
    if not launch.empty:
        with st.expander("📅 Launch Timeline Debate", expanded=False):
            for _, row in launch.sort_values("Value").iterrows():
                st.markdown(f"- **{row['Publisher']}**: {int(row['Value'])}")
