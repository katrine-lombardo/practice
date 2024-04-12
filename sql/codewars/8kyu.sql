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

-- 5. Write a function that takes an argument and returns the square of it. You
--    are given a table 'square' with column 'n'. Return a table with this
--    column and your result in a column named 'res'
SELECT n, (n*n) AS res FROM square;

-- 6. For this challenge you need to create a simple SELECT statement that will
--    return all columns from the people table WHERE their age is over 50. You
--    should return all people fields where their age is over 50 and order by
--    the age descending.
SELECT * FROM people
WHERE age > 50
ORDER BY age DESC;

-- 7. Given a demographics table you need to return the same table where all
--    letters are lowercase in the race column.
SELECT id, name, birthday, LOWER(race) as race FROM demographics;

-- 8. You have access to a table of monsters. Your task is to turn the numeric
--    columns (arms, legs) into equivalent hexadecimal values.
SELECT TO_HEX(legs) AS legs, TO_HEX(arms) AS arms FROM monsters;

-- 9. In this game, the hero moves from left to right. The player rolls the dice
--    and moves the number of spaces indicated by the dice two times. In SQL,
--    you will be given a table moves with columns position and roll. Return a
--    table which uses the current position of the hero and the roll (1-6) and
--    returns the new position in a column res.
SELECT (position + (roll*2)) AS res FROM moves;

-- 10. For this challenge you need to create a simple SUM statement that will
--     sum all the ages.
SELECT SUM(age) as age_sum FROM people;
