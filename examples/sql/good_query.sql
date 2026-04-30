select
  date(pay_time) as dt,
  channel_id,
  count(distinct user_id) as member_paid_user_count
from dwd_member_order_di
where dt between '2026-04-01' and '2026-04-07'
  and order_status in ('PAID', 'FINISHED')
  and product_type = 'MEMBER'
  and refund_status != 'FULL_REFUNDED'
  and is_test = 0
group by date(pay_time), channel_id
order by dt, channel_id;
