# Quality Rule Template

```yaml
rule_name: string
table: string
partition_field: dt
check_type: uniqueness | not_null | enum | reconciliation | fluctuation
sql: |
  select ...
severity: info | warning | critical
```
