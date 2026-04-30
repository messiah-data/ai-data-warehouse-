from __future__ import annotations

from pathlib import Path
from .io import iter_yaml_files, load_metric
from .models import MetricSpec


class MetricRegistry:
    def __init__(self, metrics: dict[str, MetricSpec]):
        self.metrics = metrics

    @classmethod
    def from_path(cls, path: str | Path) -> "MetricRegistry":
        metrics: dict[str, MetricSpec] = {}
        for file in iter_yaml_files(path):
            metric = load_metric(file)
            if metric.metric_id in metrics:
                raise ValueError(f"duplicate metric_id: {metric.metric_id}")
            metrics[metric.metric_id] = metric
        return cls(metrics)

    def get(self, metric_id: str) -> MetricSpec:
        if metric_id in self.metrics:
            return self.metrics[metric_id]
        candidates = self.search(metric_id)
        hint = f" Did you mean: {', '.join(candidates[:5])}?" if candidates else ""
        raise KeyError(f"metric not found: {metric_id}.{hint}")

    def search(self, keyword: str) -> list[str]:
        k = keyword.lower()
        result = []
        for metric_id, metric in self.metrics.items():
            haystack = " ".join([metric_id, metric.display_name, metric.description, metric.domain]).lower()
            if k in haystack:
                result.append(metric_id)
        return result

    def validate(self) -> list[str]:
        errors: list[str] = []
        for metric in self.metrics.values():
            if metric.type.value == "atomic":
                if not metric.source_table:
                    errors.append(f"{metric.metric_id}: atomic metric requires source_table")
                if not metric.expression:
                    errors.append(f"{metric.metric_id}: atomic metric requires expression")
                if not metric.time_field:
                    errors.append(f"{metric.metric_id}: atomic metric requires time_field")
            if metric.type.value in {"derived", "composite"}:
                if not metric.formula and not (metric.numerator and metric.denominator):
                    errors.append(f"{metric.metric_id}: derived/composite metric requires formula or numerator/denominator")
        return errors
