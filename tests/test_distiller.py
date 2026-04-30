from ai_dw.requirement_distiller import distill_requirement


def test_distill_member_growth():
    result = distill_requirement("需要分析会员支付转化率，按渠道和日期查看，排除测试用户")
    assert "会员" in result["entities"]
    assert "渠道" in result["dimensions"]
    assert result["candidate_metrics"]
