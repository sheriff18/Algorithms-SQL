WITH cte AS (
    SELECT e.name AS employee_name, 
           d.name AS department_name, 
           salary,
           DENSE_RANK() OVER (PARTITION BY d.id ORDER BY salary desc) AS rn
    FROM employee e
    LEFT JOIN department d ON d.id = e.departmentID 
)
SELECT  department_name AS Department,employee_name AS Employee, 
       salary
FROM cte 
WHERE rn <= 3

