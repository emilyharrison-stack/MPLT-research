"""Metric Comparison View — compare a specific metric across all analysts."""

import streamlit as st
import pandas as pd
import numpy as np

from components.charts import publisher_comparison_bar, time_series_line
from components.tables import metric_comparison_table
from components.filters import metric_selector, year_selector, therapeutic_area_filter


def render(forecasts_df: pd.DataFrame):
    """Render the Metric Comparison view."""

    st.header("Metric Comparison")
    st.caption("Compare analyst estimates for a specific metric. Spot consensus, outliers, and trends over time.")

    # --- Filters ---
    ta = therapeutic_area_filter(forecasts_df, key="mc_ta_filter")
    filtered = forecasts_df if ta is None else forecasts_df[forecasts_df["Therapeutic Area"] == ta]

    metric = metric_selector(filtered, key="mc_metric_select")
    year = year_selector(filtered, metric=metric, key="mc_year_select")

    metric_data = filtered[filtered["Metric"] == metric]
    if metric_data.empty:
        st.warning("No data available for this selection.")
        return

    unit = metric_data["Unit"].iloc[0]

    # --- Summary stats ---
    if year:
        year_data = metric_data[metric_data["Year"] == year]
    else:
        year_data = metric_data[metric_data["Year"] <= 2031]

    values = year_data["Value"]

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Analysts", len(values))
    with col2:
        st.metric("Mean", f"{values.mean():,.1f}" if len(values) > 0 else "—")
    with col3:
        st.metric("Median", f"{values.median():,.1f}" if len(values) > 0 else "—")
    with col4:
        st.metric("Low", f"{values.min():,.1f}" if len(values) > 0 else "—")
    with col5:
        st.metric("High", f"{values.max():,.1f}" if len(values) > 0 else "—")

    # Spread indicator
    if len(values) > 1 and values.median() != 0:
        spread = (values.max() - values.min()) / abs(values.median()) * 100
        if spread > 50:
            st.error(f"⚠️ High analyst disagreement — spread is {spread:.0f}% of median")
        elif spread > 25:
            st.warning(f"⚡ Moderate disagreement — spread is {spread:.0f}% of median")
        else:
            st.success(f"✅ Analysts are relatively aligned — spread is {spread:.0f}% of median")

    st.divider()

    # --- Bar chart ---
    tab1, tab2, tab3 = st.tabs(["📊 Bar Comparison", "📈 Time Series", "📋 Data Table"])

    with tab1:
        year_label = f"{year}E" if year else "All Years"
        fig = publisher_comparison_bar(
            metric_data, metric, year=year,
            title=f"{metric} — {year_label}",
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        # Only show time series for multi-year metrics
        multi_year = metric_data[metric_data["Year"] <= 2031]["Year"].nunique()
        if multi_year > 1:
            fig = time_series_line(metric_data, metric)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Time series view requires multi-year data. This metric only has single-year estimates.")

    with tab3:
        metric_comparison_table(metric_data, metric)

    # --- Outlier analysis ---
    st.divider()
    st.markdown("#### Outlier Analysis")

    if year:
        analysis_data = metric_data[metric_data["Year"] == year]
    else:
        # Use the latest year for outlier analysis
        latest_year = metric_data[metric_data["Year"] <= 2031]["Year"].max()
        analysis_data = metric_data[metric_data["Year"] == latest_year]

    if len(analysis_data) >= 3:
        mean = analysis_data["Value"].mean()
        std = analysis_data["Value"].std()

        for _, row in analysis_data.iterrows():
            if std > 0:
                z_score = (row["Value"] - mean) / std
                if abs(z_score) > 1.5:
                    direction = "above" if z_score > 0 else "below"
                    st.markdown(
                        f"- **{row['Publisher']}** is {abs(z_score):.1f}σ {direction} consensus "
                        f"({row['Value']:,.1f} vs. mean {mean:,.1f} {unit})"
                    )
    else:
        st.info("Need at least 3 analysts to perform outlier analysis.")
