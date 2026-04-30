from ai_dw.sql_review import SqlReviewer


def test_bad_query_fails_without_partition():
    sql = "select user_id from dwd_member_order_di where order_status = 'PAID'"
    result = SqlReviewer().review(sql)
    assert not result.passed
    assert any(i.code == "MISSING_PARTITION_FILTER" for i in result.issues)


def test_mutation_fails():
    result = SqlReviewer().review("drop table x")
    assert not result.passed
    assert any(i.code == "MUTATION_OR_DDL" for i in result.issues)


def test_good_query_passes():
    sql = "select dt, count(*) from t where dt='2026-04-01' group by dt"
    result = SqlReviewer().review(sql)
    assert result.passed
