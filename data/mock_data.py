"""Realistic mock data for the MPLT Research Dashboard.

This module generates sample data mimicking Wall Street analyst coverage
of Maplight Therapeutics (MPLT). Data includes reports, forecasts, and
competitor mentions. Replace with real data imports when available.
"""

import pandas as pd
from datetime import date
from models.types import Report, MetricForecast, CompetitorMention


# ---------------------------------------------------------------------------
# Reports — one per publisher covering Maplight
# ---------------------------------------------------------------------------

REPORTS: list[Report] = [
    Report(
        publisher="Morgan Stanley",
        analyst="David Risinger",
        date=date(2026, 3, 15),
        title="MPLT: Schizophrenia Data Supports Best-in-Class Profile",
        rating="Overweight",
        price_target=42.0,
        key_themes=[
            "Phase 2b schizophrenia data exceeded expectations on PANSS total",
            "Clean safety profile differentiates from competitors",
            "Peak sales potential of $2.5B+ in schizophrenia alone",
            "MDD opportunity provides additional upside not yet in estimates",
        ],
        investment_thesis=(
            "We see MPLT as a best-in-class opportunity in schizophrenia with a differentiated "
            "mechanism of action. The Phase 2b data showed statistically significant and clinically "
            "meaningful improvement vs. placebo. We model peak schizophrenia sales of $2.5B and "
            "believe the MDD opportunity adds $1B+ of optionality. Our $42 PT reflects a risk-adjusted "
            "DCF with 70% PoS for the schizophrenia program."
        ),
        notable_quotes=[
            "MPLT's efficacy signal is among the strongest we've seen in schizophrenia Phase 2 data in the last decade.",
            "We believe the clean metabolic profile could drive meaningful share from existing atypicals.",
        ],
    ),
    Report(
        publisher="Goldman Sachs",
        analyst="Chris Shibutani",
        date=date(2026, 3, 18),
        title="Initiating at Buy — Differentiated CNS Asset With Blockbuster Potential",
        rating="Buy",
        price_target=48.0,
        key_themes=[
            "First-mover advantage in novel mechanism for schizophrenia",
            "Large unmet need — 40% of patients inadequately treated",
            "Potential for weight-neutral profile is a key differentiator",
            "Partnership or M&A optionality adds to valuation floor",
        ],
        investment_thesis=(
            "We initiate coverage of MPLT with a Buy rating and $48 price target. The company's lead "
            "asset targets a novel pathway in schizophrenia with Phase 2b data showing robust efficacy "
            "(-8.2 pt PANSS improvement vs. placebo) and a clean safety/tolerability profile. We model "
            "peak WW sales of $3.1B in schizophrenia and see the MDD indication as meaningful upside. "
            "Our PT is based on a probability-adjusted NPV with a 12% discount rate."
        ),
        notable_quotes=[
            "We see MPLT's asset as potentially best-in-class given the combination of efficacy and tolerability.",
            "The $30B+ antipsychotic market is ripe for disruption by a truly differentiated agent.",
        ],
    ),
    Report(
        publisher="JPMorgan",
        analyst="Jessica Fye",
        date=date(2026, 3, 20),
        title="MPLT: Promising Data but Execution Risks Remain",
        rating="Neutral",
        price_target=28.0,
        key_themes=[
            "Phase 2b data encouraging but Phase 3 design uncertainty",
            "Competitive landscape intensifying with multiple entrants",
            "Cash runway sufficient through Phase 3 readout",
            "Valuation appears full at current levels on risk-adjusted basis",
        ],
        investment_thesis=(
            "We rate MPLT Neutral with a $28 PT. While Phase 2b schizophrenia data were encouraging "
            "(PANSS improvement of -7.5 pts vs. placebo on our re-analysis), we note the competitive "
            "landscape is intensifying with BMS and Neurocrine advancing assets. We model peak sales of "
            "$1.8B but apply a lower 50% PoS given Phase 3 risk. Our PT is based on a risk-adjusted "
            "NPV analysis. We would become more constructive on a successful Phase 3 interim look."
        ),
        notable_quotes=[
            "The data are encouraging but we've seen many CNS assets stumble in Phase 3.",
            "Competition from BMS's asset, which is 12 months ahead in development, is a key risk.",
        ],
    ),
    Report(
        publisher="Barclays",
        analyst="Carter Gould",
        date=date(2026, 3, 22),
        title="MPLT: Strong Efficacy, Premium Valuation — Initiating at Equal Weight",
        rating="Equal Weight",
        price_target=32.0,
        key_themes=[
            "Efficacy data impressive across multiple PANSS subscales",
            "Tolerability profile compares favorably to standard of care",
            "Peak sales estimates may be too aggressive given payer dynamics",
            "Launch execution in competitive CNS market will be critical",
        ],
        investment_thesis=(
            "We initiate MPLT at Equal Weight with a $32 PT. The Phase 2b data demonstrate clear "
            "efficacy in schizophrenia with a favorable tolerability profile. However, we are cautious "
            "on peak sales estimates given payer scrutiny in CNS and the need to demonstrate superiority "
            "vs. generics. We model peak US sales of $1.5B (below consensus) and apply 55% PoS. "
            "Our PT is based on a DCF analysis with a 11% WACC."
        ),
        notable_quotes=[
            "The tolerability data are the real story here — weight neutrality could be transformative.",
            "We see risk to consensus peak sales estimates given the payer environment for CNS drugs.",
        ],
    ),
    Report(
        publisher="Leerink Partners",
        analyst="Marc Goodman",
        date=date(2026, 3, 25),
        title="MPLT: Top Pick — Transformative CNS Platform",
        rating="Outperform",
        price_target=55.0,
        key_themes=[
            "Best-in-class efficacy AND tolerability in schizophrenia",
            "MDD represents a $5B+ market opportunity with limited competition",
            "Platform potential beyond schizophrenia and MDD",
            "M&A target — large pharma actively looking in CNS space",
        ],
        investment_thesis=(
            "We rate MPLT Outperform and add it as a Top Pick with a $55 PT. We believe the market "
            "is significantly undervaluing the breadth of MPLT's platform. Beyond schizophrenia "
            "(peak sales $3.5B), the MDD opportunity ($2B+ peak) and potential extensions into bipolar "
            "and anxiety create a platform worth $8B+ in risk-adjusted peak sales. Our bullish PT "
            "reflects 75% PoS for schizophrenia and 40% for MDD. We see MPLT as a premier M&A candidate."
        ),
        notable_quotes=[
            "This is the most compelling CNS dataset we've seen since the approval of Cobenfy.",
            "At current levels, you're essentially getting the MDD program for free.",
        ],
    ),
    Report(
        publisher="Citi",
        analyst="Yaron Werber",
        date=date(2026, 4, 1),
        title="MPLT: Data Solid but Competition Underappreciated",
        rating="Neutral",
        price_target=30.0,
        key_themes=[
            "Phase 2b data confirm target engagement and clinical benefit",
            "Competitive risk from Cobenfy (BMS) in the near term",
            "Neurocrine's asset in Phase 3 adds to competitive pressure",
            "Prefer to wait for Phase 3 design clarity before getting constructive",
        ],
        investment_thesis=(
            "We rate MPLT Neutral at $30. The Phase 2b data are solid and confirm the mechanism works. "
            "However, we believe the Street is underappreciating competitive risk — BMS's Cobenfy is "
            "already approved and Neurocrine is in Phase 3. MPLT needs to demonstrate clear superiority "
            "to gain meaningful share. We model peak sales of $1.6B with 45% PoS. "
            "We'd get more positive on clarity around the Phase 3 design and differentiation strategy."
        ),
        notable_quotes=[
            "The efficacy bar has been raised by Cobenfy — MPLT needs to show it can clear that bar in Phase 3.",
            "We see a path to $2B+ peak sales in a blue-sky scenario, but base case is more modest.",
        ],
    ),
    Report(
        publisher="Piper Sandler",
        analyst="David Amsellem",
        date=date(2026, 4, 3),
        title="MPLT: Initiate OW — Undervalued Platform With Multiple Catalysts",
        rating="Overweight",
        price_target=45.0,
        key_themes=[
            "Phase 2b PANSS data statistically robust with clinically meaningful effect size",
            "Differentiated safety profile vs. existing atypical antipsychotics",
            "Phase 3 initiation expected in Q3 2026 — key catalyst",
            "MDD Phase 2 data expected in H1 2027 provides additional catalyst",
        ],
        investment_thesis=(
            "We initiate MPLT at Overweight with a $45 PT. The Phase 2b schizophrenia data demonstrate "
            "a compelling efficacy/tolerability profile that we believe can support a best-in-class label. "
            "We model peak schizophrenia sales of $2.8B and see the MDD opportunity as underappreciated "
            "($1.5B peak potential). Our PT is based on a sum-of-parts risk-adjusted NPV with 65% PoS "
            "for schizophrenia."
        ),
        notable_quotes=[
            "MPLT sits in a sweet spot — strong efficacy data with a clean safety profile that payers should favor.",
            "The upcoming Phase 3 initiation is the key near-term catalyst.",
        ],
    ),
    Report(
        publisher="Stifel",
        analyst="Paul Matteis",
        date=date(2026, 4, 5),
        title="MPLT: Compelling Science, Attractive Setup Into Phase 3",
        rating="Buy",
        price_target=50.0,
        key_themes=[
            "Novel mechanism with strong preclinical and clinical rationale",
            "Phase 2b effect size among the largest seen in recent schizophrenia trials",
            "Manageable competitive landscape — differentiation is achievable",
            "Attractive risk/reward at current valuation",
        ],
        investment_thesis=(
            "We rate MPLT Buy with a $50 PT. The science behind MPLT's lead asset is compelling and "
            "the Phase 2b data validate the mechanism with a large effect size (-8.5 pt PANSS delta, our "
            "analysis). We model peak schizophrenia sales of $3.0B and MDD peak sales of $1.2B. Our PoS "
            "estimate of 65% for schizophrenia is above the class average given the strong Phase 2 data. "
            "We see the stock as attractively valued heading into Phase 3."
        ),
        notable_quotes=[
            "The PANSS effect size is notable and suggests a real and meaningful clinical benefit.",
            "We think the competitive narrative is overblown — MPLT can differentiate on tolerability.",
        ],
    ),
]


# ---------------------------------------------------------------------------
# Metric Forecasts — multi-year estimates by publisher
# ---------------------------------------------------------------------------

def _build_forecasts() -> list[MetricForecast]:
    """Build comprehensive metric forecasts across publishers and years."""
    forecasts: list[MetricForecast] = []

    # Schizophrenia peak sales estimates ($M) — the key metric with deliberate spread
    schiz_peak_sales = {
        "Morgan Stanley": {"2027E": 150, "2028E": 450, "2029E": 1100, "2030E": 1800, "Peak": 2500},
        "Goldman Sachs":  {"2027E": 200, "2028E": 580, "2029E": 1400, "2030E": 2200, "Peak": 3100},
        "JPMorgan":       {"2027E": 100, "2028E": 320, "2029E": 800,  "2030E": 1300, "Peak": 1800},
        "Barclays":       {"2027E": 80,  "2028E": 280, "2029E": 700,  "2030E": 1100, "Peak": 1500},
        "Leerink Partners": {"2027E": 250, "2028E": 700, "2029E": 1600, "2030E": 2500, "Peak": 3500},
        "Citi":           {"2027E": 90,  "2028E": 300, "2029E": 720,  "2030E": 1150, "Peak": 1600},
        "Piper Sandler":  {"2027E": 180, "2028E": 520, "2029E": 1250, "2030E": 2000, "Peak": 2800},
        "Stifel":         {"2027E": 190, "2028E": 560, "2029E": 1350, "2030E": 2100, "Peak": 3000},
    }

    for pub, yearly in schiz_peak_sales.items():
        for year_label, val in yearly.items():
            yr = int(year_label.replace("E", "")) if year_label != "Peak" else 2032
            forecasts.append(MetricForecast(
                publisher=pub, metric_name="Schizophrenia Revenue",
                therapeutic_area="Schizophrenia", year=yr, value=val, unit="$M",
                notes="Peak estimate" if year_label == "Peak" else None,
            ))

    # MDD peak sales estimates ($M)
    mdd_peak_sales = {
        "Morgan Stanley": {"2029E": 200, "2030E": 500, "Peak": 1000},
        "Goldman Sachs":  {"2029E": 280, "2030E": 650, "Peak": 1400},
        "JPMorgan":       {"2029E": 120, "2030E": 350, "Peak": 700},
        "Barclays":       {"2029E": 100, "2030E": 300, "Peak": 600},
        "Leerink Partners": {"2029E": 350, "2030E": 800, "Peak": 2000},
        "Citi":           {"2029E": 110, "2030E": 280, "Peak": 550},
        "Piper Sandler":  {"2029E": 250, "2030E": 600, "Peak": 1500},
        "Stifel":         {"2029E": 220, "2030E": 520, "Peak": 1200},
    }

    for pub, yearly in mdd_peak_sales.items():
        for year_label, val in yearly.items():
            yr = int(year_label.replace("E", "")) if year_label != "Peak" else 2033
            forecasts.append(MetricForecast(
                publisher=pub, metric_name="MDD Revenue",
                therapeutic_area="MDD", year=yr, value=val, unit="$M",
                notes="Peak estimate" if year_label == "Peak" else None,
            ))

    # Total Revenue estimates ($M)
    total_rev = {
        "Morgan Stanley": {"2026E": 15, "2027E": 165, "2028E": 480, "2029E": 1320, "2030E": 2350},
        "Goldman Sachs":  {"2026E": 12, "2027E": 210, "2028E": 610, "2029E": 1700, "2030E": 2900},
        "JPMorgan":       {"2026E": 10, "2027E": 110, "2028E": 345, "2029E": 940,  "2030E": 1680},
        "Barclays":       {"2026E": 8,  "2027E": 90,  "2028E": 300, "2029E": 820,  "2030E": 1430},
        "Leerink Partners": {"2026E": 18, "2027E": 260, "2028E": 740, "2029E": 1980, "2030E": 3350},
        "Citi":           {"2026E": 9,  "2027E": 100, "2028E": 320, "2029E": 850,  "2030E": 1460},
        "Piper Sandler":  {"2026E": 14, "2027E": 190, "2028E": 550, "2029E": 1520, "2030E": 2650},
        "Stifel":         {"2026E": 13, "2027E": 200, "2028E": 590, "2029E": 1590, "2030E": 2650},
    }

    for pub, yearly in total_rev.items():
        for year_label, val in yearly.items():
            yr = int(year_label.replace("E", ""))
            forecasts.append(MetricForecast(
                publisher=pub, metric_name="Total Revenue",
                therapeutic_area="Corporate", year=yr, value=val, unit="$M",
            ))

    # EPS estimates ($/share)
    eps = {
        "Morgan Stanley": {"2026E": -3.50, "2027E": -2.10, "2028E": 0.80, "2029E": 4.20, "2030E": 8.50},
        "Goldman Sachs":  {"2026E": -3.80, "2027E": -1.80, "2028E": 1.20, "2029E": 5.10, "2030E": 10.20},
        "JPMorgan":       {"2026E": -3.60, "2027E": -2.50, "2028E": 0.10, "2029E": 2.80, "2030E": 6.00},
        "Barclays":       {"2026E": -3.70, "2027E": -2.60, "2028E": -0.20, "2029E": 2.30, "2030E": 5.20},
        "Leerink Partners": {"2026E": -3.40, "2027E": -1.50, "2028E": 1.80, "2029E": 6.00, "2030E": 12.00},
        "Citi":           {"2026E": -3.65, "2027E": -2.40, "2028E": 0.00, "2029E": 2.50, "2030E": 5.50},
        "Piper Sandler":  {"2026E": -3.55, "2027E": -1.90, "2028E": 1.00, "2029E": 4.50, "2030E": 9.00},
        "Stifel":         {"2026E": -3.45, "2027E": -1.70, "2028E": 1.10, "2029E": 4.80, "2030E": 9.50},
    }

    for pub, yearly in eps.items():
        for year_label, val in yearly.items():
            yr = int(year_label.replace("E", ""))
            forecasts.append(MetricForecast(
                publisher=pub, metric_name="EPS",
                therapeutic_area="Corporate", year=yr, value=val, unit="$/share",
            ))

    # Probability of Success (%) for schizophrenia Phase 3
    pos = {
        "Morgan Stanley": 70,
        "Goldman Sachs": 72,
        "JPMorgan": 50,
        "Barclays": 55,
        "Leerink Partners": 75,
        "Citi": 45,
        "Piper Sandler": 65,
        "Stifel": 65,
    }

    for pub, val in pos.items():
        forecasts.append(MetricForecast(
            publisher=pub, metric_name="Schizophrenia Phase 3 PoS",
            therapeutic_area="Schizophrenia", year=2026, value=val, unit="%",
        ))

    # Price targets (duplicated from reports for easy metric comparison)
    for r in REPORTS:
        forecasts.append(MetricForecast(
            publisher=r.publisher, metric_name="Price Target",
            therapeutic_area="Corporate", year=2026, value=r.price_target, unit="$",
        ))

    # Expected launch year for schizophrenia — deliberate timeline disagreement
    launch_years = {
        "Morgan Stanley": 2029,
        "Goldman Sachs": 2029,
        "JPMorgan": 2030,
        "Barclays": 2030,
        "Leerink Partners": 2028,
        "Citi": 2030,
        "Piper Sandler": 2029,
        "Stifel": 2029,
    }

    for pub, yr in launch_years.items():
        forecasts.append(MetricForecast(
            publisher=pub, metric_name="Schizophrenia Launch Year",
            therapeutic_area="Schizophrenia", year=2026, value=float(yr), unit="Year",
            notes="Expected FDA approval / commercial launch year",
        ))

    return forecasts


FORECASTS: list[MetricForecast] = _build_forecasts()


# ---------------------------------------------------------------------------
# Competitor Mentions — how BMS / Neurocrine / Acadia analysts mention MPLT
# ---------------------------------------------------------------------------

COMPETITOR_MENTIONS: list[CompetitorMention] = [
    CompetitorMention(
        publisher="Evercore ISI",
        competitor="BMS",
        date=date(2026, 3, 10),
        context=(
            "We note that Maplight's Phase 2b data in schizophrenia represent a potential competitive "
            "threat to Cobenfy's market positioning, though we believe BMS's first-mover advantage "
            "and established commercial infrastructure provide a meaningful moat."
        ),
        sentiment="neutral",
        topic="Competitive threat to Cobenfy",
    ),
    CompetitorMention(
        publisher="RBC Capital Markets",
        competitor="Neurocrine",
        date=date(2026, 3, 12),
        context=(
            "Maplight's tolerability data could pose challenges for Neurocrine's schizophrenia asset "
            "if confirmed in Phase 3. The weight-neutral profile, if maintained, would be a meaningful "
            "differentiator that could pressure Neurocrine's market share assumptions."
        ),
        sentiment="negative",
        topic="Tolerability comparison — risk to Neurocrine",
    ),
    CompetitorMention(
        publisher="TD Cowen",
        competitor="Acadia",
        date=date(2026, 3, 28),
        context=(
            "We continue to see Acadia's pimavanserin as well-positioned in Parkinson's psychosis. "
            "While Maplight has shown promising schizophrenia data, we view the overlap as limited "
            "given distinct target patient populations."
        ),
        sentiment="neutral",
        topic="Limited competitive overlap in patient populations",
    ),
    CompetitorMention(
        publisher="Wells Fargo",
        competitor="BMS",
        date=date(2026, 4, 2),
        context=(
            "The emergence of Maplight as a credible competitor in schizophrenia is a modest negative "
            "for BMS's Cobenfy franchise. We trim our Cobenfy peak sales estimate by 5% to $6.5B to "
            "reflect incremental competitive risk from MPLT and other entrants."
        ),
        sentiment="positive",
        topic="MPLT seen as credible competitor — trims BMS estimates",
    ),
    CompetitorMention(
        publisher="BMO Capital Markets",
        competitor="Neurocrine",
        date=date(2026, 4, 4),
        context=(
            "Maplight's clean Phase 2b data raise the bar for Neurocrine's Phase 3 readout. Investors "
            "will now compare efficacy and tolerability head-to-head. We see this as incrementally "
            "negative for Neurocrine's risk/reward into their data catalyst."
        ),
        sentiment="negative",
        topic="Raises efficacy/tolerability bar for Neurocrine",
    ),
]


# ---------------------------------------------------------------------------
# Helper: convert to DataFrames for easy use in Streamlit
# ---------------------------------------------------------------------------

def get_reports_df() -> pd.DataFrame:
    """Return reports as a DataFrame."""
    rows = []
    for r in REPORTS:
        rows.append({
            "Publisher": r.publisher,
            "Analyst": r.analyst,
            "Date": r.date,
            "Title": r.title,
            "Rating": r.rating,
            "Price Target": r.price_target,
            "Key Themes": r.key_themes,
            "Investment Thesis": r.investment_thesis,
            "Notable Quotes": r.notable_quotes,
        })
    return pd.DataFrame(rows)


def get_forecasts_df() -> pd.DataFrame:
    """Return forecasts as a DataFrame."""
    rows = []
    for f in FORECASTS:
        rows.append({
            "Publisher": f.publisher,
            "Metric": f.metric_name,
            "Therapeutic Area": f.therapeutic_area,
            "Year": f.year,
            "Value": f.value,
            "Unit": f.unit,
            "Notes": f.notes,
        })
    return pd.DataFrame(rows)


def get_competitor_mentions_df() -> pd.DataFrame:
    """Return competitor mentions as a DataFrame."""
    rows = []
    for c in COMPETITOR_MENTIONS:
        rows.append({
            "Publisher": c.publisher,
            "Competitor": c.competitor,
            "Date": c.date,
            "Context": c.context,
            "Sentiment": c.sentiment,
            "Topic": c.topic,
        })
    return pd.DataFrame(rows)
