from __future__ import annotations

from jinja2 import Template
from .models import MetricSpec

ATOMIC_METRIC_SQL = Template("""
select
  {{ time_expr }} as dt{% for dim in dimensions %},
  {{ dim }}{% endfor %},
  {{ metric.expression }} as {{ alias }}
from {{ metric.source_table }}
where {{ metric.time_field }} >= '{{ start_dt }}'
  and {{ metric.time_field }} < '{{ end_dt }}'
{% for f in metric.filters %}  and {{ f }}
{% endfor %}{% for f in extra_filters %}  and {{ f }}
{% endfor %}group by {{ time_expr }}{% for dim in dimensions %}, {{ dim }}{% endfor %}
order by dt{% for dim in dimensions %}, {{ dim }}{% endfor %}
""")


def build_atomic_metric_sql(metric: MetricSpec, start_dt: str, end_dt: str, dimensions: list[str] | None = None, extra_filters: list[str] | None = None, alias: str | None = None) -> str:
    if metric.type.value != "atomic":
        raise ValueError("build_atomic_metric_sql only supports atomic metrics")
    if not metric.source_table or not metric.expression or not metric.time_field:
        raise ValueError(f"metric {metric.metric_id} lacks source_table/expression/time_field")
    dimensions = dimensions or []
    extra_filters = extra_filters or []
    unsupported = [d for d in dimensions if d not in metric.dimensions]
    if unsupported:
        raise ValueError(f"unsupported dimensions for {metric.metric_id}: {unsupported}")
    return ATOMIC_METRIC_SQL.render(metric=metric, start_dt=start_dt, end_dt=end_dt, dimensions=dimensions, extra_filters=extra_filters, alias=alias or metric.metric_id.split(".")[-1], time_expr=f"date({metric.time_field})").strip() + ";\n"
