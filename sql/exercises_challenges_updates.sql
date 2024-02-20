-- 01. Insert some data into a table
-- The club is adding a new facility - a spa. We need to add it into the facilities table. Use the following values:
-- facid: 9, Name: 'Spa', membercost: 20, guestcost: 30, initialoutlay: 100000, monthlymaintenance: 800.
INSERT INTO cd.facilities (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance) VALUES
(9, 'Spa', 20, 30, 100000, 800);

-- 02. Insert multiple rows of data into a table
INSERT INTO cd.facilities (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance) VALUES
(9, 'Spa', 20, 30, 100000, 800),
(10, 'Squash Court 2', 3.5, 17.5, 5000, 80);


-- 03. Insert calculated data into a table



-- 04. Update some existing data



-- 05. Update multiple rows and columns at the same time



-- 06. Update a row based on the contents of another row



-- 07. Delete all bookings



-- 08. Delete a member from the cd.members table



-- 09. Delete based on a subquery
