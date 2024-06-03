# Write your MySQL query statement below
select contest_id,round(count(contest_id)/(select count(distinct user_id) from users) *100,2) as percentage
from register r
group by 1
order by 2 desc, 1 asc