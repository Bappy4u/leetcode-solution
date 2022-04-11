# Write your MySQL query statement below
SELECT employee_id from Salaries where employee_id NOT IN (SELECT employee_id FROM Employees)
UNION
SELECT employee_id from Employees where employee_id NOT IN (SELECT employee_id FROM Salaries) ORDER BY employee_id;