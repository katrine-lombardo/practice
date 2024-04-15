-- 1. You are given a table random\_string. The text field holds a single row
--    which contains a random string. Your task is to take the random string and
--    split it on each vowel (a, e, i, o, u) then the resultant substrings will
--    be contained in the output table.
--  Note that the vowels should be removed. If there are no vowels, there will
--    only be one row returned. Where there are multiple vowels in succession,
--    you will see empty rows. A row should be created on each break, whether
--    there is content in the row or not.
--  Regex is advised but not mandatory.
SELECT unnest(REGEXP_SPLIT_TO_ARRAY(text,'[aeiou]'))
AS results
FROM random_string;
-- or
SELECT
  REGEXP_SPLIT_TO_TABLE(text, '[aeiou]') AS results
FROM random_string;

-- 2. Given a table of random numbers, your job is to return a table in where
--    each value is the number of bytes in the string representation of the
--    number.
SELECT
  LENGTH(number1::text) AS octnum1,
  LENGTH(number2::text) AS octnum2,
  LENGTH(number3::text) AS octnum3,
  LENGTH(number4::text) AS octnum4,
  LENGTH(number5::text) AS octnum5
FROM numbers;

-- 3. You have access to a table of monsters. Your task is to make a new table
--    where each column should contain the length of the string in the column to
--    its right (last column should contain length of string in the first
--    column). Remember some column values are not currently strings. Column
--    order and titles should remain unchanged.
SELECT
  LENGTH(CAST(name AS varchar)) AS id,
  LENGTH(CAST(legs AS varchar)) AS name,
  LENGTH(CAST(arms AS varchar)) AS legs,
  LENGTH(CAST(characteristics AS varchar)) AS arms,
  LENGTH(CAST(id AS varchar)) AS characteristics
FROM monsters;
-- or
SELECT
  LENGTH(name::varchar) AS id,
  LENGTH(legs::varchar) AS name,
  LENGTH(arms::varchar) AS legs,
  LENGTH(characteristics::varchar) AS arms,
  LENGTH(id::varchar) AS characteristics
FROM monsters;

-- 4. Given the table 'decimals' return a table with two columns (cuberoot,
--    logarithm) where the values in cuberoot are the cube root of those
--    provided in number1 and the values in logarithm are changed to the natural
--    logarithm of those in number2.
SELECT
  CBRT(number1) AS cuberoot,
  LN(number2) AS logarithm
FROM decimals;

-- 5. Complete the function that takes an integer and calculates how many dots
--    exist in a pentagonal shape around the center dot on the Nth iteration.
--    The first iteration is only a single dot. On the second, there are 6 dots.
--    On the third, there are 16 dots, and on the fourth there are 31 dots. The
--    sequence is: 1, 6, 16, 31... If the input is equal to or less than 0,
--    return -1. You are given a table 'pentagonal' with column 'n' (the bounds
--    in SQL translation: -1000 <= n <= 10^5) Return a table with all this column
--    and your result in a column named 'res'.
SELECT
    n,
    CASE
        WHEN n <= 0 THEN -1
        ELSE ((5*n^2 - 5*n + 2)/2)::BIGINT
    END AS res
FROM
    pentagonal;
-- or
SELECT
  n,
  CASE
    WHEN n <= 0 THEN -1
    ELSE (5 * (n * (n - 1)/2) + 1)
  END AS res
FROM pentagonal;

-- 6. The monsters in the provided table have too many characteristics, they
--    really only need one each. Your job is to trim the characteristics down so
--    that each monster only has one. If there is only one already, provide
--    that. If there are multiple, provide only the first one (don't leave any
--    commas in there). You must return a table with the format (id, name,
--    characteristic) and Order by id.
SELECT
  id,
  name,
  SUBSTRING(characteristics, '^[^,]+') AS characteristic
FROM monsters
ORDER BY id;
