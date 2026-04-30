---
name: data-quality-checker
description: generate and validate data quality rules for data warehouse tables and metrics, including null checks, uniqueness, enum validation, partition completeness, metric reconciliation, trend fluctuation, and anomaly detection. use when the user asks for quality checks, acceptance sql, reconciliation rules, or monitoring rules for dwd, dws, or ads tables.
---

# Data Quality Checker

## Workflow

1. Identify table grain and partition field.
2. Generate row count and partition completeness checks.
3. Generate primary grain uniqueness checks.
4. Generate null and enum checks for important fields.
5. Generate metric reconciliation checks between DWD, DWS, and ADS.
6. Generate fluctuation checks for key metrics.
