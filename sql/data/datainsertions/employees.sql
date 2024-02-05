-- CREATE TABLES
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    salary INTEGER,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255),
    start_date DATE,
    end_date DATE,
    budget INTEGER
);

CREATE TABLE IF NOT EXISTS employees_projects (
    project_id INTEGER,
    employee_id INTEGER,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);


-- INSERT DATA
INSERT INTO employees (id, first_name, last_name, salary, department_id) VALUES
(1, 'John', 'Smith', 20000, 1),
(2, 'Ava', 'Muffinson', 10000, 5),
(3, 'Cailin', 'Ninson', 30000, 2),
(4, 'Mike', 'Peterson', 20000, 2),
(5, 'Ian', 'Peterson', 80000, 2),
(6, 'John', 'Mills', 50000, 3);

INSERT INTO departments (id, name) VALUES
(1, 'Reporting'),
(2, 'Engineering'),
(3, 'Marketing'),
(4, 'Biz Dev'),
(5, 'Silly Walks');

INSERT INTO projects (id, title, start_date, end_date, budget) VALUES
(1, 'Build a cool site', 2011-10-28, 2012-01-26, 1000000),
(2, 'Update TPS Reports', 2011-07-20, 2011-10-28, 100000),
(3, 'Design 3 New Silly Walks', 2009-05-11, 2009-08-19, 100);

INSERT INTO employees_projects (project_id, employee_id) VALUES
(2, 1),
(3, 2),
(1, 3),
(1, 4),
(1, 5);
