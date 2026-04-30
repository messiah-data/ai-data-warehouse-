from __future__ import annotations

from dataclasses import dataclass, asdict
from .requirement_distiller import distill_requirement


@dataclass
class WarehouseModelSpec:
    domain: str
    source_tables: list[str]
    dwd_tables: list[str]
    dws_tables: list[str]
    ads_tables: list[str]
    quality_rules: list[str]
    acceptance_sql: list[str]


def guess_domain(text: str) -> str:
    if "会员" in text:
        return "member_growth"
    if "订单" in text or "支付" in text or "GMV" in text:
        return "trade"
    if "用户" in text or "活跃" in text:
        return "user"
    return "general"


def generate_model_spec(text: str) -> dict:
    distilled = distill_requirement(text)
    domain = guess_domain(text)
    if domain == "member_growth":
        spec = WarehouseModelSpec(
            domain=domain,
            source_tables=["ods_app_event_log_di", "ods_order_info_di", "ods_member_info_di"],
            dwd_tables=["dwd_user_event_di", "dwd_member_order_di", "dwd_member_user_status_di"],
            dws_tables=["dws_member_user_behavior_1d", "dws_member_channel_conversion_1d"],
            ads_tables=["ads_member_growth_dashboard_di", "ads_member_conversion_analysis_di"],
            quality_rules=[
                "dwd_member_order_di.order_id must be unique within dt",
                "dws_member_channel_conversion_1d.visit_uv >= paid_uv",
                "ads_member_growth_dashboard_di.member_payment_conversion_rate between 0 and 1",
            ],
            acceptance_sql=[
                "select dt, count(*) from ads_member_growth_dashboard_di where dt = '${biz_date}' group by dt;",
                "select * from ads_member_growth_dashboard_di where dt = '${biz_date}' limit 100;",
            ],
        )
    else:
        spec = WarehouseModelSpec(domain, ["ods_event_log_di"], [f"dwd_{domain}_event_di"], [f"dws_{domain}_summary_1d"], [f"ads_{domain}_dashboard_di"], ["partition row count must be greater than zero"], [f"select dt, count(*) from ads_{domain}_dashboard_di where dt = '${{biz_date}}' group by dt;"])
    result = asdict(spec)
    result["distilled_requirement"] = distilled
    return result
