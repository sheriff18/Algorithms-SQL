# Write your MySQL query statement below
select 
    query_name, round(sum(rating/position)/count(position),2) as quality, 
    round( count(case when rating < 3 then rating end) /count(rating) * 100,2)
     as poor_query_percentage
from queries
where query_name is not null
group by query_name
