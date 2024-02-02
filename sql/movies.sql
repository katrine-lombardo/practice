-- CREATE TABLES
CREATE TABLE movie (
    id INTEGER NOT NULL UNIQUE,
    title VARCHAR(70),
    yr DECIMAL(4),
    director INTEGER REFERENCES actor(id),
    budget INTEGER,
    gross INTEGER
);

CREATE TABLE actor (
    id INTEGER,
    name VARCHAR(36),
    PRIMARY KEY (id)
);

CREATE TABLE casting (
    movieid INTEGER REFERENCES movie(id),
    actorid INTEGER REFERENCES actor(id),
    ord INTEGER
);

-- INSERT DATA
INSERT INTO movie (id, title, yr, director, budget, gross) VALUES
(10003, '"Crocodile" Dundee II', 1988, 38, 15800000, 239606210),
(10004, '"Til There Was You', 1997, 49, 10000000, NULL);

INSERT INTO actor (id, name) VALUES
(20, 'Paul Hogan'),
(50, 'Jeanne Tripplehorn');

INSERT INTO casting (movieid, actorid, ord) VALUES
(10003, 20, 4),
(10004, 50, 1);
