select distinct l1.num as ConsecutiveNums
from logs l1
join logs l2 on l2.id = 1 + l1.id
join logs l3 on l3.id = 1 + l2.id
where l2.num = l1.num and l2.num = l3.num

