---
name: sql-reviewer-starrocks
description: review starrocks sql for safety, correctness, metric consistency, partition filters, join grain, performance risks, and read-only policy. use before executing ai-generated sql, when the user asks to audit sql, optimize starrocks queries, or check whether sql follows warehouse and metric rules.
---

# SQL Reviewer StarRocks

## Review Checklist

1. Is the SQL read-only?
2. Does it include partition filters for partitioned tables?
3. Does each JOIN include an ON condition?
4. Is the metric expression consistent with the registered definition?
5. Is there duplicate-counting risk?
6. Does detail SQL include LIMIT?
7. Are sensitive fields exposed?
8. Are high-cardinality group-by fields necessary?
