select m.name
from employee e
join employee m
on  e.managerid=m.id
group by e.managerid
having count(*) >=5