# Write your MySQL query statement below
delete a.*
from person a
join person b on b.email = a.email
where a.id > b.id