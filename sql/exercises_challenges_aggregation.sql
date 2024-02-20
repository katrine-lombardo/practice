-- 01. Count the number of facilities
SELECT COUNT(facid) FROM cd.facilities;

-- 02. Count the number of expensive facilities
-- Produce a count of the number of facilities that have a cost to guests of 10 or more.
SELECT COUNT(facid)
FROM cd.facilities
WHERE guestcost>=10;

-- 03. Count the number of recommendations each member makes.
-- Produce a count of the number of recommendations each member has made. Order by member ID.
SELECT recommendedby, COUNT(memid)
FROM cd.members
WHERE recommendedby IS NOT NULL
GROUP BY recommendedby
ORDER BY recommendedby;


-- 04. List the total slots booked per facility
-- Produce a list of the total number of slots booked per facility. For now, just produce an output table consisting of facility id and slots, sorted by facility id.
SELECT facid, SUM(slots) AS "Total Slots"
FROM cd.bookings
GROUP BY facid
ORDER BY facid;

-- 05. List the total slots booked per facility in a given month
-- Produce a list of the total number of slots booked per facility in the month of September 2012. Produce an output table consisting of facility id and slots, sorted by the number of slots.
SELECT facid, SUM(slots) AS "Total Slots"
FROM cd.bookings
WHERE DATE(starttime) BETWEEN '2012-09-01' AND '2012-09-30'
GROUP BY facid
ORDER BY SUM(slots);

-- 06. List the total slots booked per facility per month



-- 07. Find the count of members who have made at least one booking



-- 08. List facilities with more than 1000 slots booked



-- 09. Find the total revenue of each facility



-- 10. Find facilities with a total revenue less than 1000



-- 11. Output the facility id that has the highest number of slots booked



-- 12. List the total slots booked per facility per month, part 2



-- 13. List the total hours booked per named facility



-- 14. List each member's first booking after September 1st 2012



-- 15. Produce a list of member names, with each row containing the total member count



-- 16. Produce a numbered list of members



-- 17. Output the facility id that has the highest number of slots booked, again



-- 18. Rank members by (rounded) hours used



-- 19. Find the top three revenue generating facilities



-- 20. Classify facilities by value



-- 21. Calculate the payback time for each facility



-- 22. Calculate a rolling average of total revenue
