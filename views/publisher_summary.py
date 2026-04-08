"""Publisher Summary View — deep dive into a single analyst's report."""

import streamlit as st
import pandas as pd

from components.charts import consensus_vs_publisher_bar, publisher_comparison_bar
from components.filters import publisher_selector


def render(reports_df: pd.DataFrame, forecasts_df: pd.DataFrame):
    """Render the Publisher Summary view."""

    st.header("Publisher Summary")
    st.caption("Select a publisher to review their full report, forecasts, and how they compare to consensus.")

    publisher = publisher_selector(reports_df, key="pub_summary_select")

    report = reports_df[reports_df["Publisher"] == publisher].iloc[0]

    # --- Report header ---
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        rating = report["Rating"]
        bullish = {"Overweight", "Buy", "Outperform"}
        bearish = {"Underweight", "Sell", "Underperform"}
        if rating in bullish:
            st.metric("Rating", f"🟢 {rating}")
        elif rating in bearish:
            st.metric("Rating", f"🔴 {rating}")
        else:
            st.metric("Rating", f"🟡 {rating}")
    with col2:
        st.metric("Price Target", f"${report['Price Target']:.0f}")
    with col3:
        st.metric("Analyst", report["Analyst"])
    with col4:
        st.metric("Date", pd.to_datetime(report["Date"]).strftime("%b %d, %Y"))

    st.divider()

    # --- Title ---
    st.subheader(report["Title"])

    # --- Investment thesis ---
    st.markdown("#### Investment Thesis")
    st.markdown(report["Investment Thesis"])

    # --- Key themes ---
    st.markdown("#### Key Themes")
    for theme in report["Key Themes"]:
        st.markdown(f"- {theme}")

    # --- Notable quotes ---
    if report["Notable Quotes"]:
        st.markdown("#### Notable Quotes")
        for quote in report["Notable Quotes"]:
            st.markdown(f"> *\"{quote}\"*")

    st.divider()

    # --- Forecasts from this publisher ---
    st.markdown("#### Forecasts")

    pub_forecasts = forecasts_df[forecasts_df["Publisher"] == publisher]
    pub_forecasts_display = pub_forecasts[pub_forecasts["Year"] <= 2031].copy()

    metrics_available = sorted(pub_forecasts_display["Metric"].unique())

    for metric in metrics_available:
        metric_data = pub_forecasts_display[pub_forecasts_display["Metric"] == metric]
        if metric_data.empty:
            continue

        unit = metric_data["Unit"].iloc[0]

        with st.expander(f"📊 {metric} ({unit})", expanded=(metric == "Schizophrenia Revenue")):
            # Show table of this publisher's estimates
            pivot = metric_data.pivot_table(index="Publisher", columns="Year", values="Value", aggfunc="first")
            pivot.columns = [f"{int(y)}E" for y in pivot.columns]
            st.dataframe(pivot, use_container_width=True, hide_index=False)

            # Show vs consensus chart
            fig = consensus_vs_publisher_bar(forecasts_df, publisher, metric)
            st.plotly_chart(fig, use_container_width=True)

    # --- Where this publisher sits relative to peers ---
    st.divider()
    st.markdown("#### Price Target vs. Peers")
    fig = publisher_comparison_bar(forecasts_df, "Price Target", year=2026,
                                    title="Price Target Comparison ($)")
    st.plotly_chart(fig, use_container_width=True)
