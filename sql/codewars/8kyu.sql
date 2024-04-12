-- 1. You received an invitation to an amazing party. Now you need to write an
--    insert statement to add yourself to the table of participants.
INSERT INTO participants (name, age, attending)
VALUES ('Katrine', 32, TRUE);
SELECT * FROM participants;

-- 2. You are working for a local school, and you are responsible for collecting
--    tuition from students. You have a list of all students, some of them have
--    already paid tution and some haven't. Write a select statement to get a
--    list of all students who haven't paid their tuition yet. The list should
--    include all the data available about these students.
SELECT * FROM students
WHERE tuition_received = FALSE;

-- 3. Given the table 'decimals' return a table with one column (mod) which is
--    the output of number1 modulus number2.
SELECT (number1 % number2) as mod FROM decimals;

-- 4. Given a month as an integer from 1 to 12, return to which quarter of the
--    year it belongs as an integer number. For example: month 2 (February), is
--    part of the first quarter; month 6 (June), is part of the second quarter;
--    and month 11 (November), is part of the fourth quarter.
--    You are given a table 'quarterof' with column 'month', return a table with
--    column 'month' and your result in a column named 'res'.
SELECT month, CEIL(month/3.0)::int AS res FROM quarterof;
