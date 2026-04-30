---
name: business-knowledge-distiller
description: distill business knowledge from requirement documents, prds, meeting notes, metric requests, event tracking documents, and historical analysis into structured domains, entities, processes, candidate metrics, dimensions, filters, ambiguity lists, and confirmation questions. use when the user asks to extract business rules, summarize requirements for data work, identify metric candidates, or convert documents into reusable data warehouse knowledge.
---

# Business Knowledge Distiller

## Workflow

1. Read the requirement or business document.
2. Extract entities, events, business processes, dimensions, candidate metrics, filters, and status rules.
3. Mark ambiguity instead of inventing missing definitions.
4. Output structured YAML using references/extraction-schema.md.
5. For metrics, produce candidate definitions only. Formal metrics must be confirmed by the metric-definition-manager skill.

## Rules

- Do not treat every business noun as a table.
- Separate business facts from assumptions.
- For rate metrics, always ask for numerator, denominator, time field, and filters.
- For amount metrics, always ask whether refunds, cancelled orders, test data, and coupons are included.
