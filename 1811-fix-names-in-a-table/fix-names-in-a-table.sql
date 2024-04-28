SELECT user_id, CONCAT(UPPER(substring(name,1,1)),LOWER(substring(name,2,LENGTH(name)-1))) as name
from users
order by user_id