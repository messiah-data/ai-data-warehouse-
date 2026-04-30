from __future__ import annotations

from enum import Enum
from typing import Any, Literal
from pydantic import BaseModel, Field


class MetricType(str, Enum):
    atomic = "atomic"
    derived = "derived"
    composite = "composite"
    analytical = "analytical"


class MetricStatus(str, Enum):
    candidate = "candidate"
    active = "active"
    deprecated = "deprecated"


class FieldSpec(BaseModel):
    name: str
    type: str
    description: str = ""
    nullable: bool = True
    enum: list[str] | None = None


class TableSpec(BaseModel):
    table_name: str
    layer: Literal["ods", "dwd", "dim", "dws", "ads", "app"]
    domain: str
    description: str
    grain: str
    partition_field: str = "dt"
    primary_time_field: str | None = None
    owner: str | None = None
    fields: list[FieldSpec] = Field(default_factory=list)
    common_filters: dict[str, list[str]] = Field(default_factory=dict)


class MetricSpec(BaseModel):
    metric_id: str
    display_name: str
    domain: str
    type: MetricType
    status: MetricStatus = MetricStatus.active
    description: str
    source_table: str | None = None
    expression: str | None = None
    time_field: str | None = None
    filters: list[str] = Field(default_factory=list)
    dimensions: list[str] = Field(default_factory=list)
    formula: str | None = None
    numerator: str | None = None
    denominator: str | None = None
    owner: str | None = None
    version: str = "1.0.0"
    metadata: dict[str, Any] = Field(default_factory=dict)


class SqlReviewIssue(BaseModel):
    severity: Literal["info", "warning", "error", "critical"]
    code: str
    message: str
    suggestion: str | None = None


class SqlReviewResult(BaseModel):
    passed: bool
    issues: list[SqlReviewIssue] = Field(default_factory=list)
