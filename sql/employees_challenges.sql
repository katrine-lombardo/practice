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


---------------------------- JUNIOR INTERVIEW PREP ----------------------------
-- 5. Write a SQL query to retrieve the first name, last name, and salary of all employees in the ‘Sales’ department.


-- 6. Write a SQL query to retrieve the names of all employees who are working on a project with a budget of more than $100,000.


-- 7. Write a SQL query to retrieve the names of all employees who are not working on any project.


-- 8. Write a SQL query to retrieve the names of all employees who are working on a project that started before January 1, 2022 and ended after December 31, 2022.


-- 9. Write a SQL query to retrieve the names of all employees who are working on more than one project.


------------------------- INTERMEDIATE INTERVIEW PREP -------------------------
-- 10. Write a query to display the total salary of employees in each department.


-- 11. Write a query to find the titles of all projects that have at least one employee assigned to them.


-- 12. Write a query to find the names of all employees who have worked on a project with a budget greater than $100,000.


-- 13. Write a query to find the average salary of employees in each department, sorted by department name in ascending order.


-- 14. Write a query to find the number of employees who have worked on each project.
