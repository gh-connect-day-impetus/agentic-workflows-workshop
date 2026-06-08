select
  c.customer_id,
  sum(e.amount) as daily_revenue
from mart.customers c
join fact.events e
  on c.customer_id = e.customer_id
 and e.event_date = current_date - interval '1 day'
where c.is_active = true
group by c.customer_id;

