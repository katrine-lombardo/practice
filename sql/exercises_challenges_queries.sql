-- SIMPLE SQL QUERIES

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
-- You, for some reason, want a combined list of all surnames and all facility names. Yes, this is a contrived example :-). Produce that list!
SELECT surname FROM cd.members
UNION
SELECT name FROM cd.facilities;

-- 11. Simple aggregation
-- You'd like to get the signup date of your last member. How can you retrieve this information?
SELECT MAX(joindate) AS latest FROM cd.members;

-- 12. More aggregation
-- You'd like to get the first and last name of the last member(s) who signed up - not just the date. How can you do that?
SELECT firstname, surname, joindate FROM cd.members
WHERE joindate = (
    SELECT MAX(joindate) FROM cd.members
);


-------------------------------------------------------------------------------
-- JOINS AND SUBQUERIES
-- 01. Retrieve the start times of members' bookings
--     How can you produce a list of the start times for bookings by members
--     named 'David Farrell'?
SELECT starttime FROM cd.bookings AS b
JOIN cd.members AS m ON (m.memid = b.memid)
WHERE m.firstname = 'David' AND m.surname = 'Farrell';

-- 02. Work out the start times of bookings for tennis courts
-- How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.
SELECT starttime AS start, name FROM cd.bookings AS b
JOIN cd.facilities AS f ON (b.facid=f.facid)
WHERE DATE(starttime) = '2012-09-21'
    AND name LIKE '%Tennis Court%'
ORDER BY starttime;

-- 03. Produce a list of all members who have recommended another member
-- How can you output a list of all members who have recommended another member? Ensure that there are no duplicates in the list, and that results are ordered by (surname, firstname).
SELECT DISTINCT referrer.firstname, referrer.surname
    FROM cd.members AS referrer
JOIN cd.members AS member ON (member.recommendedby=referrer.memid)
GROUP BY referrer.memid
ORDER BY surname, firstname;

-- 04. Produce a list of all members, along with their recommender
-- How can you output a list of all members, including the individual who recommended them (if any)? Ensure that results are ordered by (surname, firstname).
SELECT mem.firstname AS memfname,
    mem.surname AS memsname,
    rec.firstname AS recfname,
    rec.surname AS recsname
FROM cd.members AS mem
LEFT JOIN cd.members AS rec ON (mem.recommendedby=rec.memid)
ORDER BY memsname, memfname;

-- 05. Produce a list of all members who have used a tennis court
-- How can you produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name followed by the facility name.
SELECT DISTINCT CONCAT(firstname, ' ', surname) AS member, name AS facility
FROM cd.members AS m
JOIN cd.bookings AS b ON (m.memid=b.memid)
JOIN cd.facilities AS f ON (b.facid=f.facid)
WHERE f.name LIKE '%Tennis Court%'
ORDER BY member, facility;

-- 06. Produce a list of costly bookings
-- How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries.
SELECT CONCAT(m.firstname, ' ', m.surname) AS member,
	f.name AS facility,
	CASE WHEN m.memid=0
		THEN b.slots * f.guestcost
		ELSE b.slots * f.membercost
		END
	AS cost
	FROM cd.members AS m
JOIN cd.bookings AS b ON (m.memid=b.memid)
JOIN cd.facilities AS f ON (b.facid=f.facid)
WHERE DATE(starttime)='2012-09-14'
	AND (
	  (m.memid=0 AND b.slots * f.guestcost > 30)
	  OR
	  (m.memid!=0 AND b.slots * f.membercost > 30)
	 )
ORDER BY cost DESC;

-- 07. Produce a list of all members, along with their recommender, using no
--     joins.
-- How can you output a list of all members, including the individual who recommended them (if any), without using any joins? Ensure that there are no duplicates in the list, and that each firstname + surname pairing is formatted as a column and ordered.
-- Using a left join:
    -- SELECT DISTINCT CONCAT(m.firstname, ' ', m.surname) AS member,
    -- 	CONCAT(recommender.firstname, ' ', recommender.surname) AS recommender
    -- 	FROM cd.members AS m
    -- LEFT JOIN cd.members AS recommender ON (m.recommendedby=recommender.memid)
    -- ORDER BY member;
-- Using a subquery:
SELECT DISTINCT CONCAT(m.firstname, ' ', m.surname) AS member, (
    SELECT CONCAT(recs.firstname, ' ', recs.surname) AS recommender
    FROM cd.members AS recs
    WHERE m.recommendedby=recs.memid
    )
    FROM cd.members AS m
ORDER BY member;

-- 08. Produce a list of costly bookings, using a subquery
-- The Produce a list of costly bookings exercise contained some messy logic: we had to calculate the booking cost in both the WHERE clause and the CASE statement. Try to simplify this calculation using subqueries.
SELECT member, facility, cost from (
    SELECT
        CONCAT(m.firstname, ' ', m.surname) AS member,
        f.name AS facility,
        CASE
            WHEN m.memid=0 THEN b.slots * f.guestcost
            ELSE b.slots * f.membercost
            END
        AS cost
    FROM cd.members AS m
        JOIN cd.bookings AS b ON (m.memid=b.memid)
        JOIN cd.facilities AS f ON (b.facid=f.facid)
    WHERE DATE(starttime)='2012-09-14'
    ) AS bookings
WHERE cost > 30
ORDER BY cost DESC;
