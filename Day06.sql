
CREATE DATABASE DAY06;

USE DAY06;

CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Salary DECIMAL(10,2),
    DepartmentID INT
);
 
CREATE TABLE Departments (
    DepartmentID INT,
    DepartmentName VARCHAR(50),
    MinSalary DECIMAL(10,2)
);
 
INSERT INTO Employees VALUES (1, 'John Doe', 50000, 101), (2, 'Jane Smith', 40000, 102);
INSERT INTO Departments VALUES (101, 'HR', 45000), (102, 'Marketing', 35000);
 
Select * from Employees
 
Select * from Departments
 
 
Select Name, Salary, DepartmentName,  MinSalary
From Employees
Inner Join Departments 
on Salary > MinSalary;


USE Hexaware;

-- Top 3 Purc_Amt
-- Clue: Read Docs

-- Solution 1
SELECT TOP 3 *
FROM orders
ORDER BY purch_amt DESC;

-- Solution 2
SELECT *
FROM ORDERS
ORDER BY PURCH_AMT DESC
OFFSET 0 ROWS FETCH NEXT 3 ROWS ONLY;

-- Task 2
-- Format Date - 25 Apr 2012

select format(ord_date,'dd mm yyyy') from orders;

SELECT FORMAT(ord_date,'D', 'en-gb' ) FROM orders;

-- Modify the satement - Asking the new user - Top n orders
DECLARE @t INT = 3;
SELECT *, FORMAT(ord_date, 'dd MMM yyyy')
FROM orders 
Order by purch_amt desc
    OFFSET 0 ROWS  
    FETCH NEXT @t ROWS ONLY;
