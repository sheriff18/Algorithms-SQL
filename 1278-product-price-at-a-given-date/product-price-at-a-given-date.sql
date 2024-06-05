# Write your MySQL query statement below
select 
    product_id, new_price as price
from    
    products
where (product_id,change_date) in (
    select 
        product_id,
        max(change_date)
    from products
    where change_date <= '2019-08-16'
    group by product_id
)

union all

select 
    product_id, 10 as new_price
from 
    products
group by 1
having min(change_date) > '2019-08-16'