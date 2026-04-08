"""Styled data table components for the MPLT Research Dashboard."""

import streamlit as st
import pandas as pd
import numpy as np


def format_value(val, unit: str) -> str:
    """Format a numeric value with its unit."""
    if pd.isna(val):
        return "—"
    if unit == "$M":
        if abs(val) >= 1000:
            return f"${val / 1000:,.1f}B"
        return f"${val:,.0f}M"
    if unit == "$B":
        return f"${val:,.1f}B"
    if unit == "$/share":
        return f"${val:,.2f}"
    if unit == "$":
        return f"${val:,.0f}"
    if unit == "%":
        return f"{val:.0f}%"
    if unit == "Year":
        return f"{int(val)}"
    return f"{val:,.1f}"


def metric_comparison_table(df: pd.DataFrame, metric: str) -> None:
    """Display a styled comparison table for a metric across publishers."""
    subset = df[df["Metric"] == metric].copy()
    subset = subset[subset["Year"] <= 2031]

    if subset.empty:
        st.info("No data available for this metric.")
        return

    unit = subset["Unit"].iloc[0]

    # Pivot: publishers as rows, years as columns
    pivot = subset.pivot_table(index="Publisher", columns="Year", values="Value", aggfunc="first")
    pivot.columns = [f"{int(y)}E" for y in pivot.columns]

    # Add consensus row
    consensus = pivot.mean(numeric_only=True)
    consensus.name = "📊 Consensus (Mean)"
    pivot = pd.concat([pivot, consensus.to_frame().T])

    # Add delta from consensus
    for col in pivot.columns:
        mean_val = consensus[col]
        pivot[f"Δ {col}"] = pivot[col].apply(
            lambda x: f"{((x - mean_val) / abs(mean_val) * 100):+.0f}%"
            if pd.notna(x) and mean_val != 0 else "—"
        )

    # Format the value columns
    display_df = pivot.copy()
    for col in [c for c in display_df.columns if not c.startswith("Δ")]:
        display_df[col] = display_df[col].apply(lambda x: format_value(x, unit))

    # Reorder columns: alternating value and delta
    ordered_cols = []
    for col in [c for c in pivot.columns if not c.startswith("Δ")]:
        ordered_cols.append(col)
        delta_col = f"Δ {col}"
        if delta_col in display_df.columns:
            ordered_cols.append(delta_col)

    st.dataframe(display_df[ordered_cols], use_container_width=True, height=400)


def report_overview_table(reports_df: pd.DataFrame) -> None:
    """Display a summary table of all reports."""
    display = reports_df[["Publisher", "Analyst", "Date", "Rating", "Price Target"]].copy()
    display["Date"] = pd.to_datetime(display["Date"]).dt.strftime("%b %d, %Y")
    display["Price Target"] = display["Price Target"].apply(lambda x: f"${x:.0f}")

    # Color-code ratings
    def rating_color(rating: str) -> str:
        bullish = {"Overweight", "Buy", "Outperform"}
        bearish = {"Underweight", "Sell", "Underperform"}
        if rating in bullish:
            return f"🟢 {rating}"
        elif rating in bearish:
            return f"🔴 {rating}"
        return f"🟡 {rating}"

    display["Rating"] = display["Rating"].apply(rating_color)
    st.dataframe(display, use_container_width=True, hide_index=True)


def inconsistency_table(inconsistencies: list[dict]) -> None:
    """Display a table of flagged inconsistencies sorted by severity."""
    if not inconsistencies:
        st.success("No significant inconsistencies detected.")
        return

    df = pd.DataFrame(inconsistencies)

    # Sort by severity
    severity_order = {"High": 0, "Medium": 1, "Low": 2}
    df["_sort"] = df["Severity"].map(severity_order)
    df = df.sort_values("_sort").drop("_sort", axis=1)

    def severity_icon(s: str) -> str:
        icons = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
        return f"{icons.get(s, '')} {s}"

    df["Severity"] = df["Severity"].apply(severity_icon)

    st.dataframe(df, use_container_width=True, hide_index=True, height=400)
