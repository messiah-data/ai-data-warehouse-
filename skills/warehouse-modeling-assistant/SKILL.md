---
name: warehouse-modeling-assistant
description: design ai-assisted data warehouse models from business requirements, including ods, dwd, dim, dws, ads layers, table grain, starrocks ddl, etl sql, metric mapping, lineage, data quality rules, and acceptance sql. use when the user asks to build data marts, design dwd/dws/ads tables, convert requirements into warehouse models, or generate starrocks table schemas and etl logic.
---

# Warehouse Modeling Assistant

## Workflow

1. Extract business goals, entities, events, dimensions, and metrics from requirements.
2. Identify source tables and missing data.
3. Design layer-by-layer models: ODS, DWD, DIM, DWS, ADS.
4. Specify table grain before fields.
5. Generate StarRocks DDL with partitioning and distribution strategy.
6. Generate ETL SQL and scheduling dependencies.
7. Generate data quality rules and acceptance SQL.
8. List open questions and risks.
