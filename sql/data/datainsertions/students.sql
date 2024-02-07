-- Create Courses table
CREATE TABLE Courses (
  CourseID INT PRIMARY KEY,
  CourseName VARCHAR(50)
);

-- Create Students table
CREATE TABLE Students (
  StudentID INT PRIMARY KEY,
  StudentName VARCHAR(50),
  CourseID INT,
  FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Insert data into Courses
INSERT INTO Courses (CourseID, CourseName) VALUES
(1, 'Mathematics'),
(2, 'Physics'),
(3, 'Chemistry');

-- Insert data into Students
INSERT INTO Students (StudentID, StudentName, CourseID) VALUES
(1, 'Alice', 1),
(2, 'Bob', 1),
(3, 'Charlie', 2),
(4, 'David', 3),
(5, 'Eva', NULL);
