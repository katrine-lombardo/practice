-- CREATE TABLES
CREATE TABLE game (
    id INTEGER PRIMARY KEY,
    mdate TEXT NOT NULL,
    stadium TEXT NOT NULL,
    team1 TEXT NOT NULL,
    team2 TEXT NOT NULL
);

CREATE TABLE goal (
    matchid INTEGER,
    teamid TEXT,
    player TEXT NOT NULL,
    gtime INTEGER NOT NULL,
    FOREIGN KEY (matchid) REFERENCES game(id),
    FOREIGN KEY (teamid) REFERENCES eteam(id)
);

CREATE TABLE eteam (
    id TEXT PRIMARY KEY,
    teamname TEXT NOT NULL,
    coach TEXT NOT NULL
);


-- INSERT DATA
INSERT INTO game (id, mdate, stadium, team1, team2) VALUES
(1001, '8 June 2012', 'National Stadium, Warsaw', 'POL', 'GRE'),
(1002, '8 June 2012', 'Stadion Miejski (Wroclaw)', 'RUS', 'CZE'),
(1003, '12 June 2012', 'Stadion Miejski (Wroclaw)', 'GRE', 'CZE'),
(1004, '12 June 2012', 'National Stadium, Warsaw', 'POL', 'RUS');

INSERT INTO goal (matchid, teamid, player, gtime) VALUES
(1001, 'POL', 'Robert Lewandowski', 17),
(1001, 'GRE', 'Dimitris Salpingidis', 51),
(1002, 'RUS', 'Alan Dzagoev', 15),
(1002, 'RUS', 'Roman Pavlyuchenko', 82);

INSERT INTO eteam (id, teamname, coach) VALUES
('POL', 'Poland', 'Franciszek Smuda'),
('RUS', 'Russia', 'Dick Advocaat'),
('CZE', 'Czech Republic', 'Michal Bilek'),
('GRE', 'Greece', 'Fernando Santos');
