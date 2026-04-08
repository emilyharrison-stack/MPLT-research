"""MPLT Research Dashboard — Interactive analyst report comparison tool.

Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd

from data.mock_data import get_reports_df, get_forecasts_df, get_competitor_mentions_df
from views import publisher_summary, metric_comparison, inconsistency_detector

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="MPLT Research Dashboard",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Load data (cached)
# ---------------------------------------------------------------------------

@st.cache_data
def load_data():
    return get_reports_df(), get_forecasts_df(), get_competitor_mentions_df()

reports_df, forecasts_df, mentions_df = load_data()

# ---------------------------------------------------------------------------
# Sidebar — navigation
# ---------------------------------------------------------------------------
st.sidebar.title("🔬 MPLT Research")
st.sidebar.caption("Maplight Therapeutics — Analyst Dashboard")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    ["📋 Overview", "🏦 Publisher Summary", "📊 Metric Comparison",
     "⚠️ Inconsistency Detector", "🔍 Competitor Mentions"],
    key="nav",
)

st.sidebar.divider()
st.sidebar.caption(f"Covering {len(reports_df)} analyst reports")
st.sidebar.caption("Data: Mock (replace with real data)")

# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

if page == "📋 Overview":
    st.title("MPLT Research Dashboard")
    st.markdown("**Maplight Therapeutics** — Analyst Report Comparison & Insights")
    st.divider()

    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Analysts Covering", len(reports_df))
    with col2:
        consensus_pt = reports_df["Price Target"].mean()
        st.metric("Consensus PT", f"${consensus_pt:.0f}")
    with col3:
        pt_range = f"${reports_df['Price Target'].min():.0f} – ${reports_df['Price Target'].max():.0f}"
        st.metric("PT Range", pt_range)
    with col4:
        bullish = sum(1 for r in reports_df["Rating"]
                      if r in {"Overweight", "Buy", "Outperform"})
        st.metric("Bullish Ratings", f"{bullish}/{len(reports_df)}")

    st.divider()

    # Reports table
    st.markdown("### All Analyst Reports")
    from components.tables import report_overview_table
    report_overview_table(reports_df)

    st.divider()

    # Quick charts
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("### Price Target Distribution")
        from components.charts import publisher_comparison_bar
        fig = publisher_comparison_bar(forecasts_df, "Price Target", year=2026)
        st.plotly_chart(fig, use_container_width=True)

    with col_b:
        st.markdown("### Schizophrenia Peak Sales")
        peak = forecasts_df[(forecasts_df["Metric"] == "Schizophrenia Revenue") &
                            (forecasts_df["Year"] > 2031)]
        if not peak.empty:
            fig = publisher_comparison_bar(peak, "Schizophrenia Revenue",
                                           title="Schizophrenia Peak Sales ($M)")
            st.plotly_chart(fig, use_container_width=True)

    # Key themes across all reports
    st.divider()
    st.markdown("### Key Themes Across All Reports")

    all_themes = []
    for _, row in reports_df.iterrows():
        for theme in row["Key Themes"]:
            all_themes.append({"Publisher": row["Publisher"], "Theme": theme})

    themes_df = pd.DataFrame(all_themes)
    st.dataframe(themes_df, use_container_width=True, hide_index=True)


elif page == "🏦 Publisher Summary":
    publisher_summary.render(reports_df, forecasts_df)


elif page == "📊 Metric Comparison":
    metric_comparison.render(forecasts_df)


elif page == "⚠️ Inconsistency Detector":
    inconsistency_detector.render(forecasts_df, reports_df)


elif page == "🔍 Competitor Mentions":
    st.header("Competitor Mentions")
    st.caption("How analysts covering BMS, Neurocrine, and Acadia mention Maplight Therapeutics.")

    # Filter
    competitors = sorted(mentions_df["Competitor"].unique())
    selected = st.selectbox("Filter by Competitor", ["All"] + competitors)

    filtered = mentions_df if selected == "All" else mentions_df[mentions_df["Competitor"] == selected]

    # Summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Mentions", len(filtered))
    with col2:
        positive = len(filtered[filtered["Sentiment"] == "positive"])
        st.metric("Positive", positive)
    with col3:
        negative = len(filtered[filtered["Sentiment"] == "negative"])
        st.metric("Negative", negative)

    st.divider()

    # Mention cards
    for _, row in filtered.iterrows():
        sentiment_icon = {"positive": "🟢", "neutral": "🟡", "negative": "🔴"}.get(row["Sentiment"], "⚪")
        with st.expander(
            f"{sentiment_icon} **{row['Publisher']}** (covering {row['Competitor']}) — {row['Topic']}",
            expanded=True,
        ):
            st.markdown(f"*{pd.to_datetime(row['Date']).strftime('%b %d, %Y')}*")
            st.markdown(f"> {row['Context']}")
            st.markdown(f"**Sentiment:** {row['Sentiment'].title()} | **Topic:** {row['Topic']}")
