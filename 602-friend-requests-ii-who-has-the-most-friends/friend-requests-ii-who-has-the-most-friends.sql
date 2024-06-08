# Write your MySQL query statement below
with cte as(select requester_id as user_id
from requestaccepted
union all
select accepter_id as user_id
from requestaccepted),
cte2 as(
    select user_id, count(user_id) as cnt,
    rank() over (order by count(user_id) desc) as rnk
    from cte
    group by 1
)

select user_id as id, cnt as num
from cte2
where rnk = 1