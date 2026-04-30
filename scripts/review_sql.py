#!/usr/bin/env python3
from pathlib import Path
import sys
from rich.console import Console
from ai_dw.sql_review import SqlReviewer

console = Console()


def main():
    if len(sys.argv) < 2:
        console.print("usage: python scripts/review_sql.py <sql-file>")
        raise SystemExit(2)
    sql = Path(sys.argv[1]).read_text(encoding="utf-8")
    result = SqlReviewer().review(sql)
    console.print(f"passed: {result.passed}")
    for issue in result.issues:
        console.print(f"[{issue.severity}] {issue.code}: {issue.message}")
        if issue.suggestion:
            console.print(f"  suggestion: {issue.suggestion}")
    raise SystemExit(0 if result.passed else 1)

if __name__ == "__main__":
    main()
