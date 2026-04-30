from __future__ import annotations

import re
import sqlparse
from .models import SqlReviewIssue, SqlReviewResult

DANGEROUS = re.compile(r"\b(drop|truncate|delete|update|insert|alter|grant|revoke|create)\b", re.I)
READONLY_START = re.compile(r"^\s*(select|with|show|describe|desc|explain)\b", re.I)
PARTITION_HINT = re.compile(r"\b(dt|ds|biz_date|p_date)\s*(=|between|>=|<=|in)\b", re.I)
LIMIT_HINT = re.compile(r"\blimit\s+\d+\b", re.I)
JOIN_WITHOUT_ON = re.compile(r"\bjoin\b(?![\s\S]{0,180}?\bon\b)", re.I)


class SqlReviewer:
    def __init__(self, require_partition: bool = True, require_limit_for_detail: bool = True):
        self.require_partition = require_partition
        self.require_limit_for_detail = require_limit_for_detail

    def review(self, sql: str) -> SqlReviewResult:
        issues: list[SqlReviewIssue] = []
        statements = [s.strip() for s in sqlparse.split(sql) if s.strip()]
        if not statements:
            return SqlReviewResult(passed=False, issues=[SqlReviewIssue(severity="error", code="EMPTY_SQL", message="SQL is empty")])
        if len(statements) > 1:
            issues.append(SqlReviewIssue(severity="warning", code="MULTI_STATEMENT", message="SQL contains multiple statements."))
        for stmt in statements:
            if DANGEROUS.search(stmt):
                issues.append(SqlReviewIssue(severity="critical", code="MUTATION_OR_DDL", message="SQL contains DDL or DML keywords.", suggestion="Use read-only SQL or require explicit approval."))
            if not READONLY_START.search(stmt):
                issues.append(SqlReviewIssue(severity="error", code="NOT_READONLY_START", message="SQL does not start with an allowed read-only keyword."))
            if self.require_partition and re.search(r"\bfrom\b", stmt, re.I) and not PARTITION_HINT.search(stmt):
                issues.append(SqlReviewIssue(severity="error", code="MISSING_PARTITION_FILTER", message="Query appears to scan a table without a partition filter.", suggestion="Add dt/ds/biz_date/p_date predicate."))
            if JOIN_WITHOUT_ON.search(stmt):
                issues.append(SqlReviewIssue(severity="error", code="JOIN_WITHOUT_ON", message="JOIN may be missing an ON condition."))
            has_group = re.search(r"\bgroup\s+by\b", stmt, re.I)
            has_agg = re.search(r"\b(count|sum|avg|min|max)\s*\(", stmt, re.I)
            if self.require_limit_for_detail and re.search(r"\bselect\b", stmt, re.I) and not has_group and not has_agg and not LIMIT_HINT.search(stmt):
                issues.append(SqlReviewIssue(severity="warning", code="DETAIL_QUERY_WITHOUT_LIMIT", message="Detail query has no LIMIT.", suggestion="Add LIMIT for detail inspection queries."))
        passed = not any(i.severity in {"error", "critical"} for i in issues)
        return SqlReviewResult(passed=passed, issues=issues)
