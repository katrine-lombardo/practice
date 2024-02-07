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
-- 5. Write a SQL query to retrieve the first name, last name, and salary of all
--    employees in the ‘Sales’ department.
SELECT first_name, last_name, salary FROM employees
INNER JOIN departments ON (employees.department_id=departments.id)
WHERE departments.name='Sales';

-- 6. Write a SQL query to retrieve the names of all employees who are working on a project with a budget of more than $100,000.
SELECT CONCAT(first_name, ' ', last_name) as full_name FROM employees
INNER JOIN employees_projects ON (employee_id=employees.id)
INNER JOIN projects ON (project_id=projects.id)
WHERE projects.budget > 100000;

-- 7. Write a SQL query to retrieve the names of all employees who are not working on any project.
SELECT CONCAT(first_name, ' ', last_name) AS "employees not on any projects" FROM employees
LEFT JOIN employees_projects AS ep ON (employee_id=employees.id)
WHERE ep.project_id IS NULL;

-- 8. Write a SQL query to retrieve the names of all employees who are working on a project that started before January 1, 2022 and ended after December 31, 2022.
--    NOTES: It might be easier to start with a table of names, start dates, and
--    end dates. Note wordong of question:
--    From there, filter to keep start dates before 1/1/22, and keep end dates after 12/31/22.
SELECT CONCAT(first_name, ' ', last_name) AS "ees on projects in 2022" FROM employees
LEFT JOIN employees_projects AS ep ON (ep.employee_id=employees.id)
LEFT JOIN projects AS p ON (ep.project_id=p.id)
WHERE p.start_date<'2022-01-01' AND p.end_date>'2022-12-31';

-- 9. Write a SQL query to retrieve the names of all employees who are working
--    on more than one project.
--    NOTE: I'm including the additional column for number of projects as this
--    contextual information may be relevant given the nature of the question.
SELECT CONCAT(first_name, ' ', last_name) AS "ees on more than one project", COUNT(ep.project_id) AS "num of projects"
FROM employees AS e
INNER JOIN employees_projects AS ep ON e.id = ep.employee_id
GROUP BY e.id, e.first_name, e.last_name
HAVING COUNT(ep.project_id) > 1
ORDER BY "ees on more than one project";
-- Without the num of projects column:
SELECT CONCAT(first_name, ' ', last_name) AS "ees on more than one project"
FROM employees AS e
INNER JOIN employees_projects AS ep ON e.id = ep.employee_id
GROUP BY e.id, e.first_name, e.last_name
HAVING COUNT(ep.project_id) > 1
ORDER BY "ees on more than one project";


------------------------- INTERMEDIATE INTERVIEW PREP -------------------------
-- 10. Write a query to display the total salary of employees in each department.


-- 11. Write a query to find the titles of all projects that have at least one employee assigned to them.


-- 12. Write a query to find the names of all employees who have worked on a project with a budget greater than $100,000.


-- 13. Write a query to find the average salary of employees in each department, sorted by department name in ascending order.


-- 14. Write a query to find the number of employees who have worked on each project.
