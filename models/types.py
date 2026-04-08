"""Data types for the MPLT Research Dashboard."""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Publisher:
    name: str
    analyst: str
    firm_type: str  # "bulge_bracket", "boutique", "specialist"


@dataclass
class Report:
    publisher: str
    analyst: str
    date: date
    title: str
    rating: str  # "Overweight", "Buy", "Neutral", "Hold", "Underweight", "Sell"
    price_target: float
    key_themes: list[str]
    investment_thesis: str
    notable_quotes: list[str] = field(default_factory=list)


@dataclass
class MetricForecast:
    publisher: str
    metric_name: str
    therapeutic_area: str  # "Schizophrenia", "MDD", "Corporate", etc.
    year: int
    value: float
    unit: str  # "$M", "$B", "$/share", "%", "patients"
    notes: Optional[str] = None


@dataclass
class CompetitorMention:
    publisher: str  # The firm whose report mentions Maplight
    competitor: str  # Which competitor's report it comes from (BMS, Neurocrine, Acadia)
    date: date
    context: str  # Quote or snippet mentioning Maplight
    sentiment: str  # "positive", "neutral", "negative"
    topic: str  # What aspect they mentioned (pipeline, competitive threat, etc.)
