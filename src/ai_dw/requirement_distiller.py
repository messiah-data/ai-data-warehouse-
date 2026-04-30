from __future__ import annotations

import re
from dataclasses import dataclass, asdict

ENTITY_WORDS = ["用户", "会员", "订单", "商品", "优惠券", "渠道", "内容", "支付", "退款", "访问"]
METRIC_PATTERNS = [r"[\u4e00-\u9fa5A-Za-z0-9_]*(?:率|数|金额|GMV|UV|PV|留存|转化|复购)[\u4e00-\u9fa5A-Za-z0-9_]*"]
DIMENSION_WORDS = ["日期", "渠道", "城市", "省份", "会员等级", "新老用户", "版本", "平台", "端", "商品类目"]


@dataclass
class DistilledRequirement:
    title: str
    entities: list[str]
    candidate_metrics: list[str]
    dimensions: list[str]
    business_rules: list[str]
    open_questions: list[str]


def distill_requirement(text: str, title: str = "requirement") -> dict:
    entities = [w for w in ENTITY_WORDS if w in text]
    metrics: set[str] = set()
    for pattern in METRIC_PATTERNS:
        for m in re.findall(pattern, text):
            if len(m) >= 2:
                metrics.add(m)
    dimensions = [w for w in DIMENSION_WORDS if w in text]
    rules = []
    for line in text.splitlines():
        if any(k in line for k in ["排除", "不包含", "仅统计", "过滤", "口径", "状态"]):
            rules.append(line.strip(" -"))
    open_questions = []
    for metric in sorted(metrics):
        if "率" in metric or "转化" in metric:
            open_questions.append(f"请确认 {metric} 的分子、分母、时间字段和过滤条件。")
        if "金额" in metric or "GMV" in metric:
            open_questions.append(f"请确认 {metric} 是否包含退款、取消订单、测试订单。")
    return asdict(DistilledRequirement(title, entities, sorted(metrics), dimensions, rules, open_questions))
