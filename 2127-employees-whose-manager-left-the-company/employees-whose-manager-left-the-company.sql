# Write your MySQL query statement below
select employee_id
from employees
where salary < 30000 and  manager_id not in (
    select employee_id
    from employees
)
order by 1 asc