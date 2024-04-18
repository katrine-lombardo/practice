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
