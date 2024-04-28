-- EASY (1-5)

-- 1. Give the organiser's name of the concert in the Assembly Rooms after the
--    first of Feb, 1997.
SELECT m_name FROM musician AS m
JOIN concert AS c ON (c.concert_orgniser = m.m_no)
WHERE c.concert_venue = 'Assembly Rooms'
    AND c.con_date > 02/01/1997;

-- 2. Find all the performers who played guitar or violin and were born in
--    England.


-- 3. List the names of musicians who have conducted concerts in USA together
--    with the towns and dates of these concerts.


-- 4. How many concerts have featured at least one composition by Andy Jones?
--    List concert date, venue and the composition's title.


-- 5. List the different instruments played by the musicians and avg number of
--    musicians who play the instrument.






-- MEDIUM (6-10)


-- DIFFICULT (11-15)
