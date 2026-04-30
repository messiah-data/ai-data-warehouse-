from __future__ import annotations

from pathlib import Path
import yaml
from .models import MetricSpec, TableSpec


def load_yaml(path: str | Path) -> dict:
    with Path(path).open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object")
    return data


def load_metric(path: str | Path) -> MetricSpec:
    return MetricSpec.model_validate(load_yaml(path))


def load_table(path: str | Path) -> TableSpec:
    return TableSpec.model_validate(load_yaml(path))


def iter_yaml_files(path: str | Path):
    p = Path(path)
    if p.is_file():
        yield p
        return
    for suffix in ("*.yaml", "*.yml"):
        for item in sorted(p.rglob(suffix)):
            yield item
