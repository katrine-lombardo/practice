-- Simple SQL Queries
-- 01. Retrieve everything from a table
-- How can you retrieve all the information from the cd.facilities table?
SELECT * FROM cd.facilities;

-- 02. Retrieve specific columns from a table
--     You want to print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs?
SELECT name, membercost FROM cd.facilities;

-- 03. Control which rows are retrieved
-- How can you produce a list of facilities that charge a fee to members?
SELECT * FROM cd.facilities
WHERE membercost > 0;

-- 04. Control which rows are retrieved - part 2
--     How can you produce a list of facilities that charge a fee to members,
--     and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the
--     facilities in question.
SELECT facid, name, membercost, monthlymaintenance
FROM cd.facilities
WHERE membercost < (monthlymaintenance/50)
	AND membercost > 0;

-- 05. Basic string searches
-- How can you produce a list of all facilities with the word 'Tennis' in their name?
SELECT * FROM cd.facilities
WHERE name LIKE '%Tennis%';

-- 06. Matching against multiple possible values
-- How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.
SELECT * FROM cd.facilities
WHERE facid in (1,5);

-- 07. Classify results into buckets
-- How can you produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.
SELECT name,
	CASE WHEN (monthlymaintenance > 100)
		THEN 'expensive'
		ELSE 'cheap'
		END
	AS cost
FROM cd.facilities;

-- 08. Working with dates
-- How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, firstname, and joindate of the members in question.
SELECT memid, surname, firstname, joindate
FROM cd.members
WHERE joindate > '2012-09-01';

-- 09. Removing duplicates, and ordering results
-- How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
SELECT DISTINCT surname FROM cd.members
ORDER BY surname
LIMIT 10;

-- 10. Combining results from multiple queries

-- 11. Simple aggregation

-- 12. More aggregation
