-- 1. Query all columns for all American cities in the CITY table with
--    populations larger than 100000. The CountryCode for America is USA.
SELECT * FROM CITY
WHERE COUNTRYCODE = 'USA' AND POPULATION > 100000;

-- 2. Query the NAME field for all American cities in the CITY table with
--   populations larger than 120000. The CountryCode for America is USA.
SELECT NAME FROM CITY
WHERE POPULATION > 120000 AND COUNTRYCODE = 'USA';

-- 3. Query all columns (attributes) for every row in the CITY table.
SELECT * FROM CITY;

-- 4. Query all columns for a city in CITY with the ID 1661.
SELECT * FROM CITY
WHERE ID = 1661;

-- 5. Query all attributes of every Japanese city in the CITY table. The
--    COUNTRYCODE for Japan is JPN.
SELECT * FROM CITY
WHERE COUNTRYCODE = 'JPN';

-- 6. Query the names of all the Japanese cities in the CITY table. The
--    COUNTRYCODE for Japan is JPN.
SELECT NAME FROM CITY
WHERE COUNTRYCODE = 'JPN';

-- 7. Query a list of CITY and STATE from the STATION table.
SELECT CITY, STATE FROM STATION;

-- 8. Query a list of CITY names from STATION for cities that have an even ID
--    number. Print the results in any order, but exclude duplicates from the
--    answer.
SELECT DISTINCT CITY FROM STATION
WHERE ID % 2 = 0;

-- 9. Find the difference between the total number of CITY entries in the table
--    and the number of distinct CITY entries in the table.
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;

-- 10. Query the two cities in STATION with the shortest and longest CITY names,
--     as well as their respective lengths (i.e.: number of characters in the
--     name). If there is more than one smallest or largest city, choose the one
--     that comes first when ordered alphabetically.
(
    SELECT CITY, LENGTH(CITY)
    FROM STATION
    WHERE LENGTH(CITY) = (SELECT MIN(LENGTH(CITY)) FROM STATION)
    ORDER BY CITY
    LIMIT 1
) UNION ALL (
    SELECT CITY, LENGTH(CITY)
    FROM STATION
    WHERE LENGTH(CITY) = (SELECT MAX(LENGTH(CITY)) FROM STATION)
    ORDER BY CITY
    LIMIT 1
);

-- 11. Query the list of CITY names starting with vowels (i.e., a, e, i, o, or
--     u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[AEIOU]';

-- 12. Query the list of CITY names ending with vowels (a, e, i, o, u) from
--     STATION. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '[AEIOU]$';

-- 13. Query the list of CITY names from STATION which have vowels (i.e., a, e,
--     i, o, and u) as both their first and last characters. Your result cannot
--     contain duplicates.
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[AEIOU]' AND CITY REGEXP '[AEIOU]$';

-- 14. Query the list of CITY names from STATION that do not start with vowels.
--     Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[^AEIOU]';

-- 15. Query the list of CITY names from STATION that do not end with vowels.
--     Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '[^AEIOU]$';

-- 16. Query the list of CITY names from STATION that either do not start with
--     vowels or do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[^AEIOU]' OR CITY REGEXP '[^AEIOU]$';

-- 17. Query the list of CITY names from STATION that do not start with vowels
--     and do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[^AEIOU]' AND CITY REGEXP '[^AEIOU]$';

-- 18. Query the Name of any student in STUDENTS who scored higher than  Marks.
--     Order your output by the last three characters of each name. If two or
--     more students both have names ending in the same last three characters
--     (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
SELECT Name FROM STUDENTS
WHERE Marks > 75
ORDER BY SUBSTRING(Name, -3) ASC, ID ASC;

-- 19. Write a query that prints a list of employee names (i.e.: the name
--     attribute) from the Employee table in alphabetical order.
SELECT name FROM Employee
ORDER BY name;

-- 20. Write a query that prints a list of employee names (i.e.: the name
--     attribute) for employees in Employee having a salary greater than 2000 per
--     month who have been employees for less than 10 months. Sort your result by
--     ascending employee_id.
SELECT name FROM Employee
WHERE salary > 2000 AND months < 10;
