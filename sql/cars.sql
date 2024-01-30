-- CREATE TABLES

CREATE TABLE Manufacturer (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE Model (
    id INTEGER PRIMARY KEY,
    manufacturer_id INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES Manufacturer(id)
);

CREATE TABLE Automobile (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    model_id INTEGER,
    vin TEXT NOT NULL,
    FOREIGN KEY (model_id) REFERENCES Model(id)
);

CREATE TABLE Color (
    id INTEGER PRIMARY KEY,
    color TEXT NOT NULL,
    automobile_id INTEGER,
    FOREIGN KEY (automobile_id) REFERENCES Automobile(id)
);


-- INSERT DATA
INSERT INTO Manufacturer (id, name) VALUES
(1, 'Fiat-Chrysler'),
(2, 'Mercedes-Benz'),
(3, 'Toyota');

INSERT INTO Model (id, manufacturer_id, name) VALUES
(1, 1, 'Sebring'),
(2, 2, 'GL450'),
(3, 3, 'RAV4');

INSERT INTO Automobile (id, year, model_id, vin) VALUES
(1, 2009, 1, '1C3LC46BX9N530999'),
(2, 2007, 2, '4JGBF71E17A153402'),
(3, 2017, 3, '2T3BFREV4HW618087'),
(4, 2009, 1, '1C3LC46BX9N538292');

INSERT INTO Color (id, color, automobile_id) VALUES
(1, 'Gold', 1),
(2, 'Black', 2),
(3, 'Silver', 2),
(4, 'Silver', 3),
(5, 'White', 3),
(6, 'Gold', 4),
(7, 'Silver', 4);
