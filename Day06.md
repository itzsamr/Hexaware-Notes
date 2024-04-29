## Agenda - 29/04/24

1. Equi, Natural, Inner Join
2. Sub Queries -> Exists, Not Exists
3. Union, Intersection, Except
4. Limit, Offset -> MS SQL
5. Types of Keys, ACID (Theory Part)
6. Group By, Order By -> Advanced

[Select Order By Clause (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver16)

-- SET THEORY
-- UNION
-- Intersect - common
-- Except - Difference

CREATE DATABASE setoperations;

USE setoperations;

CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(50)
);
 
INSERT INTO Employees (EmployeeID, Name, Department) VALUES
(1, 'Alice', 'Engineering'),
(2, 'Bob', 'Marketing'),
(3, 'Charlie', 'Engineering'),
(4, 'Dana', 'HR');
 
 
CREATE TABLE Applicants (
    ApplicantID INT,
    Name VARCHAR(50),
    AppliedFor VARCHAR(50)
);
 
INSERT INTO Applicants (ApplicantID, Name, AppliedFor) VALUES
(5, 'George', 'Engineering'),
(6, 'Helen', 'Marketing'),
(7, 'Ian', 'Marketing'),
(3, 'Charlie', 'Sales');

-- Intersection
SELECT Department FROM Employees
INTERSECT
SELECT AppliedFor FROM Applicants;

-- Union
SELECT Department FROM Employees
UNION
SELECT AppliedFor FROM Applicants;

-- Except
SELECT Department FROM Employees
EXCEPT
SELECT AppliedFor FROM Applicants;

SELECT AppliedFor FROM Applicants
EXCEPT
SELECT Department FROM Employees;
