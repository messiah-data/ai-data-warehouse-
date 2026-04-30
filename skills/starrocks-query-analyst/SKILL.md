---
name: starrocks-query-analyst
description: analyze business data by generating safe starrocks sql, inspecting starrocks schemas through mcp, applying registered metric definitions, executing read-only queries, and explaining query results. use when the user asks for starrocks data analysis, metric calculation, table exploration, trend analysis, attribution analysis, dashboard query support, or sql generation based on business口径.
---

# StarRocks Query Analyst

## Workflow

1. Understand the business question.
2. Resolve the business domain and metric definitions before writing SQL.
3. Inspect StarRocks schema through MCP when table or field structure is uncertain.
4. Generate a query plan before generating SQL for complex analysis.
5. Review SQL with the sql-reviewer-starrocks rules.
6. Execute only read-only SQL through StarRocks MCP.
7. Summarize results with facts, inference, assumptions, and validation suggestions.

## Query Safety

- Default to SELECT/WITH/SHOW/DESCRIBE/EXPLAIN.
- Require partition filters for large tables.
- Detail queries need LIMIT.
- Do not query sensitive user-level fields unless explicitly requested and allowed.
- Do not invent metric filters.
