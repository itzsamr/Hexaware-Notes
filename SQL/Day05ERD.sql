<<<<<<< HEAD

CREATE TABLE [Professor] (
  [professor_id] Varchar(255),
  [professor_name] Varchar(255),
  [department] Varchar(255),
  PRIMARY KEY ([professor_id],
);
 
 
CREATE TABLE [Student] (
  [student_id] Varchar(255),
  [student_name] Varchar(255),
  PRIMARY KEY ([student_id])
);
 
CREATE TABLE [Course] (
  [course_id] Varchar(255),
  [course_name] Varchar(255),
  [professor_id] Varchar(255),
  PRIMARY KEY ([course_id]),
  Foreign Key ([professor_id]) References Professor([professor_id])
);
 
 
CREATE TABLE [Enrollment] (
  [enroll_id] Varchar(255) ,
  [course_id] Varchar(255),
  [student_id] Varchar(255) ,
  PRIMARY KEY ([enroll_id]),
  Foreign Key ([course_id]) References Course([course_id]),
  Foreign Key ([student_id]) References Student([student_id])
);
 
 
INSERT INTO Professor (professor_id, professor_name, department)
VALUES ('P001', 'Dr. Brown', 'Mathematics'),
       ('P002', 'Dr. Smith', 'Physics');
 
 
Select * from Professor;
 
INSERT INTO Student (student_id, student_name)
VALUES ('S001', 'Alice'),
       ('S002', 'Bob'),
       ('S003', 'Charlie');
 
Select * from Professor;
 
Select * from Course;
 
INSERT INTO Course (course_id, course_name, professor_id)
VALUES ('C001', 'Math 101', 'P001'),
       ('C002', 'Physics 101', 'P002');
 
 
INSERT INTO Enrollment (enroll_id, course_id, student_id)
VALUES ('E001', 'C001', 'S001'),
       ('E002', 'C002', 'S002'),
       ('E003', 'C002', 'S001'),
       ('E004', 'C001', 'S003');
 
Select * from Enrollment;

CREATE TABLE EmployeeData (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary INT,
    StartDate DATE
);

INSERT INTO EmployeeData (EmployeeID, FirstName, LastName, Salary, StartDate) 
VALUES
	(1, 'John', 'Doe', 70000, '2020-05-01'),
	(2, 'Jane', 'Smith', 85000, '2018-08-15'),
	(3, 'Emily', 'Jones', 94000, '2019-12-30'),
	(4, 'Chris', 'Brown', 62000, '2021-03-22');

SELECT * FROM EmployeeData;

-- Task 1
-- Sort the employees by the length of their first names in descending order.
SELECT *
FROM EmployeeData
ORDER BY LEN(FirstName) DESC;

-- Task 2
-- Get the Initials JD, JS, EJ, CB


USE Day05ERD;

SELECT GETDATE();

-- Task 4
-- Write a query to calculate the tenure of each employee in complete years as of today.

SELECT 
    *,
    DATEDIFF(YEAR, StartDate, GETDATE()) AS TenureInYears
FROM 
    EmployeeData;
=======

CREATE TABLE [Professor] (
  [professor_id] Varchar(255),
  [professor_name] Varchar(255),
  [department] Varchar(255),
  PRIMARY KEY ([professor_id],
);
 
 
CREATE TABLE [Student] (
  [student_id] Varchar(255),
  [student_name] Varchar(255),
  PRIMARY KEY ([student_id])
);
 
CREATE TABLE [Course] (
  [course_id] Varchar(255),
  [course_name] Varchar(255),
  [professor_id] Varchar(255),
  PRIMARY KEY ([course_id]),
  Foreign Key ([professor_id]) References Professor([professor_id])
);
 
 
CREATE TABLE [Enrollment] (
  [enroll_id] Varchar(255) ,
  [course_id] Varchar(255),
  [student_id] Varchar(255) ,
  PRIMARY KEY ([enroll_id]),
  Foreign Key ([course_id]) References Course([course_id]),
  Foreign Key ([student_id]) References Student([student_id])
);
 
 
INSERT INTO Professor (professor_id, professor_name, department)
VALUES ('P001', 'Dr. Brown', 'Mathematics'),
       ('P002', 'Dr. Smith', 'Physics');
 
 
Select * from Professor;
 
INSERT INTO Student (student_id, student_name)
VALUES ('S001', 'Alice'),
       ('S002', 'Bob'),
       ('S003', 'Charlie');
 
Select * from Professor;
 
Select * from Course;
 
INSERT INTO Course (course_id, course_name, professor_id)
VALUES ('C001', 'Math 101', 'P001'),
       ('C002', 'Physics 101', 'P002');
 
 
INSERT INTO Enrollment (enroll_id, course_id, student_id)
VALUES ('E001', 'C001', 'S001'),
       ('E002', 'C002', 'S002'),
       ('E003', 'C002', 'S001'),
       ('E004', 'C001', 'S003');
 
Select * from Enrollment;

CREATE TABLE EmployeeData (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary INT,
    StartDate DATE
);

INSERT INTO EmployeeData (EmployeeID, FirstName, LastName, Salary, StartDate) 
VALUES
	(1, 'John', 'Doe', 70000, '2020-05-01'),
	(2, 'Jane', 'Smith', 85000, '2018-08-15'),
	(3, 'Emily', 'Jones', 94000, '2019-12-30'),
	(4, 'Chris', 'Brown', 62000, '2021-03-22');

SELECT * FROM EmployeeData;

-- Task 1
-- Sort the employees by the length of their first names in descending order.
SELECT *
FROM EmployeeData
ORDER BY LEN(FirstName) DESC;

-- Task 2
-- Get the Initials JD, JS, EJ, CB


USE Day05ERD;

SELECT GETDATE();

-- Task 4
-- Write a query to calculate the tenure of each employee in complete years as of today.

SELECT 
    *,
    DATEDIFF(YEAR, StartDate, GETDATE()) AS TenureInYears
FROM 
    EmployeeData;
>>>>>>> b2d60b51f8db3d78d83d367f42fb4eb8e63b9e41

-- Task 5 - Calculate Annual Salary Increase
-- Assume a yearly salary increase of 3% for each employee. 
-- Write a query to calculate their new salary rounded to the nearest whole number.

<<<<<<< HEAD
SELECT 
	*,
    ROUND(Salary * 1.03, 0) AS New_Salary
FROM 
    EmployeeData;
=======
SELECT 
	*,
    ROUND(Salary * 1.03, 0) AS New_Salary
FROM 
    EmployeeData;
>>>>>>> b2d60b51f8db3d78d83d367f42fb4eb8e63b9e41
