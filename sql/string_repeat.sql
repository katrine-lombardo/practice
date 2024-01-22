-- Write a function that accepts an integer n and a string s as parameters, and
-- returns a string of s repeated exactly n times.

-- Examples (input -> output)
-- 6, "I"     -> "IIIIII"
-- 5, "Hello" -> "HelloHelloHelloHelloHello"

--# write your SQL statement here: you are given a table 'repeatstr' with columns 'n' and 's', return a table with all columns and your result in a column named 'res'.

CREATE TABLE IF NOT EXISTS repeatstr (
    id INTEGER PRIMARY KEY,
    n INT,
    s VARCHAR(255)
);

INSERT INTO repeatstr (n, s) VALUES
    (3, "*"),
    (5, "#"),
    (2, "ha");

SELECT s, n,
REPLICATE(s, n)
AS res
FROM repeatstr;
