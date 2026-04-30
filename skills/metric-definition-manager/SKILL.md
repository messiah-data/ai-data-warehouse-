---
name: metric-definition-manager
description: manage and validate business metric definitions for data warehouse analysis, including atomic metrics, derived metrics, filters, dimensions, time fields, owners, versions, and yaml registry entries. use when the user asks about metric口径, calculation logic, metric registry design, metric yaml validation, or when an analysis query requires choosing the correct metric definition before generating sql.
---

# Metric Definition Manager

## Workflow

1. Identify the metric requested by the user.
2. Search the metric registry in knowledge/metrics/.
3. If the metric exists, use its source table, expression, time field, filters, and supported dimensions.
4. If the metric is ambiguous or missing, create a candidate metric and list required confirmations.
5. Validate registry changes with scripts/validate_metric_registry.py.

## Metric Rules

- Atomic metrics require source_table, expression, and time_field.
- Derived metrics require formula or numerator and denominator.
- Never silently change filters for an active metric.
- Any changed active metric should increment version.
