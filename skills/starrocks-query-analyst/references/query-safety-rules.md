# Query Safety Rules

- Reject DDL/DML by default.
- Require dt, ds, biz_date, or equivalent partition predicates.
- Limit detail queries.
- Check join ON conditions.
- Explain metric口径 before execution.
