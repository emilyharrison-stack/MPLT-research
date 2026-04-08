"""Sidebar filter components for the MPLT Research Dashboard."""

import streamlit as st
import pandas as pd


def publisher_selector(reports_df: pd.DataFrame, key: str = "pub_select") -> str:
    """Sidebar dropdown to select a publisher."""
    publishers = sorted(reports_df["Publisher"].unique())
    return st.sidebar.selectbox("Select Publisher", publishers, key=key)


def metric_selector(forecasts_df: pd.DataFrame, key: str = "metric_select") -> str:
    """Sidebar dropdown to select a metric."""
    metrics = sorted(forecasts_df["Metric"].unique())
    return st.sidebar.selectbox("Select Metric", metrics, key=key)


def year_selector(forecasts_df: pd.DataFrame, metric: str | None = None,
                   key: str = "year_select") -> int | None:
    """Sidebar dropdown to select a year, optionally filtered by metric."""
    subset = forecasts_df
    if metric:
        subset = subset[subset["Metric"] == metric]
    years = sorted(subset[subset["Year"] <= 2031]["Year"].unique())
    if not years:
        return None
    options = ["All Years"] + [f"{y}E" for y in years]
    selected = st.sidebar.selectbox("Select Year", options, key=key)
    if selected == "All Years":
        return None
    return int(selected.replace("E", ""))


def therapeutic_area_filter(forecasts_df: pd.DataFrame,
                             key: str = "ta_filter") -> str | None:
    """Sidebar dropdown to filter by therapeutic area."""
    areas = sorted(forecasts_df["Therapeutic Area"].unique())
    options = ["All Areas"] + areas
    selected = st.sidebar.selectbox("Therapeutic Area", options, key=key)
    return None if selected == "All Areas" else selected


def competitor_filter(mentions_df: pd.DataFrame,
                       key: str = "comp_filter") -> str | None:
    """Sidebar dropdown to filter competitor mentions."""
    competitors = sorted(mentions_df["Competitor"].unique())
    options = ["All Competitors"] + competitors
    selected = st.sidebar.selectbox("Competitor", options, key=key)
    return None if selected == "All Competitors" else selected
