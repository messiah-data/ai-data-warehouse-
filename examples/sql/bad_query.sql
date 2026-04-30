select user_id, order_id, pay_amount
from dwd_member_order_di
where order_status = 'PAID';
