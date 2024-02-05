-- 1. Sort the current employees at the company by who has the highest salary
SELECT * FROM employees
ORDER BY salary DESC;

-- 2. Show all of the employees that worked on the project “Build a cool site”
SELECT CONCAT(first_name, ' ', last_name) AS name FROM employees
JOIN employees_projects ON (employee_id=employees.id)
JOIN projects ON (project_id=projects.id)
WHERE title='Build a cool site';

-- 3. For the project “Build a cool site”, if an employee was paid on the 1st and the 15th of every month, show how much each employee made for the duration of the project.
-- NOTE: Salary is not specified so I'll assume it's annual.
SELECT CONCAT(first_name, ' ', last_name) AS name, ((salary/52/5) * (END_DATE - START_DATE)) AS ee_made_how_much FROM employees
JOIN employees_projects ON (employee_id=employees.id)
JOIN projects ON (project_id=projects.id)
WHERE projects.title='Build a cool site';

-- 4. No Code Required! Talk us through how you’d break down the data to figure out who was the most valuable employee to the company
