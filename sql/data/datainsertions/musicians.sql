-- Create the band table
CREATE TABLE band (
    band_no INT PRIMARY KEY,
    band_name VARCHAR(255),
    band_home INT,
    band_type VARCHAR(255),
    b_date DATE,
    band_contact INT
);

-- Populate the band table
INSERT INTO band (band_no, band_name, band_home, band_type, b_date, band_contact)
VALUES
(1, 'ROP', 5, 'classical', '2001-01-30', 11),
(2, 'AASO', 6, 'classical', NULL, 10),
(3, 'The J Bs', 8, 'jazz', NULL, 12),
(4, 'BBSO', 9, 'classical', NULL, 21),
(5, 'The left Overs', 2, 'jazz', NULL, 8),
(6, 'Somebody Loves this', 1, 'jazz', NULL, 6),
(7, 'Oh well', 4, 'classical', NULL, 3),
(8, 'Swinging strings', 4, 'classical', NULL, 7),
(9, 'The Rest', 9, 'jazz', NULL, 16);

-- Create the composer table
CREATE TABLE composer (
    comp_no INT PRIMARY KEY,
    comp_is INT,
    comp_type VARCHAR(255)
);

-- Populate the composer table
INSERT INTO composer (comp_no, comp_is, comp_type)
VALUES
(1, 1, 'jazz'),
(2, 3, 'classical'),
(3, 5, 'jazz'),
(4, 7, 'classical'),
(5, 9, 'jazz'),
(6, 11, 'rock'),
(7, 13, 'classical'),
(8, 15, 'jazz'),
(9, 17, 'classical'),
(10, 19, 'jazz'),
(11, 10, 'rock'),
(12, 8, 'jazz');

-- Create the composition table
CREATE TABLE composition (
    c_no INT PRIMARY KEY,
    comp_date DATE,
    c_title VARCHAR(255),
    c_in INT
);

-- Populate the composition table
INSERT INTO composition (c_no, comp_date, c_title, c_in)
VALUES
(1, '1975-06-17', 'Opus 1', 1),
(2, '1976-07-21', 'Here Goes', 2),
(3, '1981-12-14', 'Valiant Knight', 3),
(4, '1982-01-12', 'Little Piece', 4),
(5, '1985-03-13', 'Simple Song', 5),
(6, '1986-04-14', 'Little Swing Song', 6),
(7, '1987-05-13', 'Fast Journey', 7),
(8, '1976-02-14', 'Simple Love Song', 8),
(9, '1982-01-21', 'Complex Rythms', 9),
(10, '1985-02-23', 'Drumming Rythms', 9),
(11, '1978-03-18', 'Fast Drumming', 8),
(12, '1984-08-13', 'Slow Song', 7),
(13, '1968-09-14', 'Blue Roses', 6),
(14, '1983-11-15', 'Velvet Rain', 5),
(15, '1982-05-16', 'Cold Wind', 4),
(16, '1983-06-18', 'After the Wind Blows', 3),
(17, NULL, 'A Simple Piece', 2),
(18, '1985-01-12', 'Long Rythms', 1),
(19, '1988-02-12', 'Eastern Wind', 1),
(20, NULL, 'Slow Symphony Blowing', 2),
(21, '1990-07-12', 'A Last Song', 6);

-- Create the concert table
CREATE TABLE concert (
    concert_no INT PRIMARY KEY,
    concert_venue VARCHAR(255),
    concert_in INT,
    con_date DATE,
    concert_orgniser INT
);

-- Populate the concert table
INSERT INTO concert (concert_no, concert_venue, concert_in, con_date, concert_orgniser)
VALUES
(1, 'Bridgewater Hall', 1, '1995-01-06', 21),
(2, 'Bridgewater Hall', 1, '1996-05-08', 3),
(3, 'Usher Hall', 2, '1995-06-03', 3),
(4, 'Assembly Rooms', 2, '1997-09-20', 21),
(5, 'Festspiel Haus', 3, '1995-02-21', 8),
(6, 'Royal Albert Hall', 7, '1993-04-12', 8),
(7, 'Concertgebouw', 9, '1993-05-14', 8),
(8, 'Metropolitan', 4, '1997-06-15', 21);

-- Create the musician table
CREATE TABLE musician (
    m_no INT PRIMARY KEY,
    m_name VARCHAR(255),
    born DATE,
    died DATE,
    born_in INT,
    living_in INT
);

-- Populate the musician table
INSERT INTO musician (m_no, m_name, born, died, born_in, living_in)
VALUES
(1, 'Fred Bloggs', '1948-01-02', NULL, 1, 2),
(2, 'John Smith', '1950-03-03', NULL, 3, 4),
(3, 'Helen Smyth', '1948-08-08', NULL, 4, 5),
(4, 'Harriet Smithson', '1909-05-09', '1980-09-20', 5, 6),
(5, 'James First', '1965-06-10', NULL, 7, 7),
(6, 'Theo Mengel', '1948-08-12', NULL, 7, 1),
(7, 'Sue Little', '1945-02-21', NULL, 8, 9),
(8, 'Harry Forte', '1951-02-28', NULL, 1, 8),
(9, 'Phil Hot', '1942-06-30', NULL, 2, 7),
(10, 'Jeff Dawn', '1945-12-12', NULL, 3, 6),
(11, 'Rose Spring', '1948-05-25', NULL, 4, 5),
(12, 'Davis Heavan', '1975-10-03', NULL, 5, 4),
(13, 'Lovely Time', '1948-12-28', NULL, 6, 3),
(14, 'Alan Fluff', '1935-01-15', '1997-05-15', 7, 2),
(15, 'Tony Smythe', '1932-04-02', NULL, 8, 1),
(16, 'James Quick', '1924-08-08', NULL, 9, 2),
(17, 'Freda Miles', '1920-07-04', NULL, 9, 3),
(18, 'Elsie James', '1947-05-06', NULL, 8, 5),
(19, 'Andy Jones', '1958-10-08', NULL, 7, 6),
(20, 'Louise Simpson', '1948-01-10', '1998-02-11', 6, 6),
(21, 'James Steeple', '1947-01-10', NULL, 5, 6),
(22, 'Steven Chaytors', '1956-03-11', NULL, 6, 7);

-- Create the performer table
CREATE TABLE performer (
    perf_no INT PRIMARY KEY,
    perf_is INT,
    instrument VARCHAR(255),
    perf_type VARCHAR(255)
);

-- Populate the performer table
INSERT INTO performer (perf_no, perf_is, instrument, perf_type)
VALUES
(1, 2, 'violin', 'classical'),
(2, 4, 'viola', 'classical'),
(3, 6, 'banjo', 'jazz'),
(4, 8, 'violin', 'classical'),
(5, 12, 'guitar', 'jazz'),
(6, 14, 'violin', 'classical'),
(7, 16, 'trumpet', 'jazz'),
(8, 18, 'viola', 'classical'),
(9, 20, 'bass', 'jazz'),
(10, 2, 'flute', 'jazz'),
(11, 20, 'cornet', 'jazz'),
(12, 6, 'violin', 'jazz'),
(13, 8, 'drums', 'jazz'),
(14, 10, 'violin', 'classical'),
(15, 12, 'cello', 'classical'),
(16, 14, 'viola', 'classical'),
(17, 16, 'flute', 'jazz'),
(18, 18, 'guitar', 'not known'),
(19, 20, 'trombone', 'jazz'),
(20, 3, 'horn', 'jazz'),
(21, 5, 'violin', 'jazz'),
(22, 7, 'cello', 'classical'),
(23, 2, 'bass', 'jazz'),
(24, 4, 'violin', 'jazz'),
(25, 6, 'drums', 'classical'),
(26, 8, 'clarinet', 'jazz'),
(27, 10, 'bass', 'jazz'),
(28, 12, 'viola', 'classical'),
(29, 18, 'cello', 'classical');

-- Create the place table
CREATE TABLE place (
    place_no INT PRIMARY KEY,
    place_town VARCHAR(255),
    place_country VARCHAR(255)
);

-- Populate the place table
INSERT INTO place (place_no, place_town, place_country)
VALUES
(1, 'Manchester', 'England'),
(2, 'Edinburgh', 'Scotland'),
(3, 'Salzburg', 'Austria'),
(4, 'New York', 'USA'),
(5, 'Birmingham', 'England'),
(6, 'Glasgow', 'Scotland'),
(7, 'London', 'England'),
(8, 'Chicago', 'USA'),
(9, 'Amsterdam', 'Netherlands');

-- Create the plays_in table
CREATE TABLE plays_in (
    player INT,
    band_id INT
);

-- Populate the plays_in table
INSERT INTO plays_in (player, band_id)
VALUES
(1, 1),
(1, 7),
(3, 1),
(4, 1),
(4, 7),
(5, 1),
(6, 1),
(6, 7),
(7, 1),
(8, 1),
(8, 7),
(10, 2),
(12, 2),
(13, 2),
(14, 2),
(14, 8),
(15, 2),
(15, 8),
(17, 2),
(18, 2),
(19, 3),
(20, 3),
(21, 4),
(22, 4),
(23, 4),
(25, 5),
(26, 6),
(27, 6),
(28, 7),
(28, 8),
(29, 7);

-- Create the has_composed table
CREATE TABLE has_composed (
    cmpr_no INT,
    cmpn_no INT
);

-- Populate the has_composed table
INSERT INTO has_composed (cmpr_no, cmpn_no)
VALUES
(1, 1),
(1, 8),
(2, 11),
(3, 2),
(3, 13),
(3, 14),
(3, 18),
(4, 12),
(4, 20),
(5, 3),
(5, 13),
(5, 14),
(6, 15),
(6, 21),
(7, 4),
(7, 9),
(8, 16),
(9, 5),
(9, 10),
(10, 17),
(11, 6),
(12, 7),
(12, 19);

-- Create the performance table
CREATE TABLE performance (
    pfrmnc_no INT PRIMARY KEY,
    gave INT,
    performed INT,
    conducted_by INT,
    performed_in INT
);

-- Populate the performance table
INSERT INTO performance (pfrmnc_no, gave, performed, conducted_by, performed_in)
VALUES
(1, 1, 1, 21, 1),
(2, 1, 3, 21, 1),
(3, 1, 5, 21, 1),
(4, 1, 2, 1, 2),
(5, 2, 4, 21, 2),
(6, 2, 6, 21, 2),
(7, 4, 19, 9, 3),
(8, 4, 20, 10, 3),
(9, 5, 12, 10, 4),
(10, 5, 13, 11, 4),
(11, 3, 5, 13, 5),
(12, 3, 6, 13, 5),
(13, 3, 7, 13, 5),
(14, 6, 20, 14, 6),
(15, 8, 12, 15, 7),
(16, 9, 16, 21, 8),
(17, 9, 17, 21, 8),
(18, 9, 18, 21, 8),
(19, 9, 19, 21, 8),
(20, 4, 12, 10, 3);
