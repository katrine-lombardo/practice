-- 1. You received an invitation to an amazing party. Now you need to write an insert statement to add yourself to the table of participants.
INSERT INTO participants (name, age, attending)
VALUES ('Katrine', 32, TRUE);
SELECT * FROM participants;

-- 2. You are working for a local school, and you are responsible for collecting tuition from students. You have a list of all students, some of them have already paid tution and some haven't. Write a select statement to get a list of all students who haven't paid their tuition yet. The list should include all the data available about these students.
SELECT * FROM students
WHERE tuition_received = FALSE;
