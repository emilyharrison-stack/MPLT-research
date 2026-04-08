"""Reusable Plotly chart components for the MPLT Research Dashboard."""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def publisher_comparison_bar(df: pd.DataFrame, metric: str, year: int | None = None,
                              title: str | None = None) -> go.Figure:
    """Bar chart comparing a metric across publishers, with consensus line."""
    subset = df[df["Metric"] == metric]
    if year is not None:
        subset = subset[subset["Year"] == year]

    if subset.empty:
        fig = go.Figure()
        fig.add_annotation(text="No data available", xref="paper", yref="paper",
                           x=0.5, y=0.5, showarrow=False, font=dict(size=16))
        return fig

    subset = subset.sort_values("Value", ascending=True)
    mean_val = subset["Value"].mean()
    median_val = subset["Value"].median()
    unit = subset["Unit"].iloc[0]

    # Color by deviation from median
    colors = []
    for val in subset["Value"]:
        pct_diff = abs(val - median_val) / abs(median_val) if median_val != 0 else 0
        if pct_diff > 0.3:
            colors.append("#ef4444")  # red — outlier
        elif pct_diff > 0.15:
            colors.append("#f59e0b")  # amber — moderate deviation
        else:
            colors.append("#3b82f6")  # blue — near consensus

    chart_title = title or f"{metric} Comparison ({unit})"
    if year and year < 2032:
        chart_title += f" — {year}E"

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=subset["Value"],
        y=subset["Publisher"],
        orientation="h",
        marker_color=colors,
        text=[f"{v:,.0f}" if abs(v) >= 10 else f"{v:,.2f}" for v in subset["Value"]],
        textposition="outside",
        hovertemplate="%{y}: %{x:,.1f} " + unit + "<extra></extra>",
    ))

    # Consensus lines
    fig.add_vline(x=mean_val, line_dash="dash", line_color="#6b7280",
                  annotation_text=f"Mean: {mean_val:,.1f}", annotation_position="top right")
    fig.add_vline(x=median_val, line_dash="dot", line_color="#9333ea",
                  annotation_text=f"Median: {median_val:,.1f}", annotation_position="bottom right")

    fig.update_layout(
        title=chart_title,
        xaxis_title=unit,
        yaxis_title="",
        height=max(350, len(subset) * 50 + 100),
        margin=dict(l=20, r=80, t=60, b=40),
        showlegend=False,
    )
    return fig


def time_series_line(df: pd.DataFrame, metric: str,
                      title: str | None = None) -> go.Figure:
    """Line chart showing a metric over time, one line per publisher."""
    subset = df[df["Metric"] == metric].copy()
    # Exclude "Peak" placeholder years
    subset = subset[subset["Year"] <= 2031]

    if subset.empty:
        fig = go.Figure()
        fig.add_annotation(text="No data available", xref="paper", yref="paper",
                           x=0.5, y=0.5, showarrow=False, font=dict(size=16))
        return fig

    unit = subset["Unit"].iloc[0]
    chart_title = title or f"{metric} Over Time ({unit})"

    fig = px.line(
        subset,
        x="Year",
        y="Value",
        color="Publisher",
        markers=True,
        title=chart_title,
        labels={"Value": unit, "Year": ""},
    )

    # Add consensus band (mean ± std)
    yearly = subset.groupby("Year")["Value"].agg(["mean", "std"]).reset_index()
    fig.add_trace(go.Scatter(
        x=yearly["Year"], y=yearly["mean"] + yearly["std"],
        mode="lines", line=dict(width=0), showlegend=False, hoverinfo="skip",
    ))
    fig.add_trace(go.Scatter(
        x=yearly["Year"], y=yearly["mean"] - yearly["std"],
        mode="lines", line=dict(width=0), fill="tonexty",
        fillcolor="rgba(147,51,234,0.1)", name="Consensus ±1σ",
        hoverinfo="skip",
    ))

    fig.update_layout(
        height=450,
        margin=dict(l=20, r=20, t=60, b=40),
        xaxis=dict(dtick=1),
    )
    return fig


def agreement_heatmap(df: pd.DataFrame, metrics: list[str] | None = None) -> go.Figure:
    """Heatmap showing coefficient of variation across metrics and years.

    Higher CV = more disagreement among analysts.
    """
    subset = df.copy()
    if metrics:
        subset = subset[subset["Metric"].isin(metrics)]

    # Exclude single-year or "peak" entries for cleaner view
    subset = subset[subset["Year"] <= 2031]

    pivot = subset.groupby(["Metric", "Year"])["Value"].agg(["mean", "std"]).reset_index()
    pivot["CV"] = (pivot["std"] / pivot["mean"].abs()).clip(0, 2) * 100  # as percentage
    pivot["CV"] = pivot["CV"].fillna(0)

    heatmap_data = pivot.pivot(index="Metric", columns="Year", values="CV").fillna(0)

    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=[str(y) + "E" for y in heatmap_data.columns],
        y=heatmap_data.index,
        colorscale=[
            [0.0, "#10b981"],    # green — consensus
            [0.3, "#fbbf24"],    # amber — some disagreement
            [0.6, "#ef4444"],    # red — high disagreement
            [1.0, "#7f1d1d"],    # dark red — extreme
        ],
        colorbar_title="Disagreement<br>(CV %)",
        hovertemplate="Metric: %{y}<br>Year: %{x}<br>CV: %{z:.1f}%<extra></extra>",
    ))

    fig.update_layout(
        title="Analyst Disagreement Heatmap (Coefficient of Variation)",
        height=max(300, len(heatmap_data) * 60 + 100),
        margin=dict(l=20, r=20, t=60, b=40),
    )
    return fig


def consensus_vs_publisher_bar(forecasts_df: pd.DataFrame, publisher: str,
                                 metric: str, year: int | None = None) -> go.Figure:
    """Show how one publisher's estimates compare to consensus for a metric."""
    subset = forecasts_df[forecasts_df["Metric"] == metric]
    if year:
        subset = subset[subset["Year"] == year]
    else:
        # Use the latest year available
        subset = subset[subset["Year"] <= 2031]

    if subset.empty:
        fig = go.Figure()
        fig.add_annotation(text="No data available", xref="paper", yref="paper",
                           x=0.5, y=0.5, showarrow=False, font=dict(size=16))
        return fig

    yearly_data = subset.groupby("Year").agg(
        consensus=("Value", "mean"),
        publisher_val=("Value", lambda x: x[subset.loc[x.index, "Publisher"] == publisher].values[0]
                        if publisher in subset.loc[x.index, "Publisher"].values else np.nan)
    ).dropna().reset_index()

    unit = subset["Unit"].iloc[0]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=yearly_data["Year"], y=yearly_data["consensus"],
        name="Consensus (Mean)", marker_color="#94a3b8",
    ))
    fig.add_trace(go.Bar(
        x=yearly_data["Year"], y=yearly_data["publisher_val"],
        name=publisher, marker_color="#3b82f6",
    ))

    fig.update_layout(
        title=f"{publisher} vs. Consensus — {metric} ({unit})",
        barmode="group",
        xaxis=dict(dtick=1),
        yaxis_title=unit,
        height=400,
        margin=dict(l=20, r=20, t=60, b=40),
    )
    return fig
