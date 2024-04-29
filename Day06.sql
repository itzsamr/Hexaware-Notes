
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

---------------------------

CREATE TABLE Products (

    ProductID INT,

    ProductName VARCHAR(50),

    Category VARCHAR(50),

    InStock CHAR(3)

);
 
INSERT INTO Products (ProductID, ProductName, Category, InStock) VALUES

(1, 'Laptop', 'Electronics', 'Yes'),

(2, 'Smartphone', 'Electronics', 'No'),

(3, 'Coffee Maker', 'Appliances', 'Yes'),

(4, 'Blender', 'Appliances', 'Yes'),

(5, 'T-shirt', 'Apparel', 'No');

CREATE TABLE Orders (

    OrderID INT,

    ProductID INT,

    CustomerName VARCHAR(50),

    Quantity INT

);
 
INSERT INTO Orders (OrderID, ProductID, CustomerName, Quantity) VALUES

(100, 1, 'Alice', 1),

(101, 3, 'Bob', 2),

(102, 2, 'Charlie', 1),

(103, 4, 'Dana', 1),

(104, 3, 'Alice', 1);

-- Task 1
-- List all distinct products that are either in stock or have been orders.

SELECT * from Orders;
SELECT * from Products;

SELECT DISTINCT ProductID, ProductName, Category
FROM (
    SELECT ProductID, ProductName, Category
    FROM Products
    WHERE InStock = 'Yes'    
    UNION    
    SELECT p.ProductID, p.ProductName, p.Category
    FROM Products p
    INNER JOIN Orders o ON p.ProductID = o.ProductID
) AS CombinedProducts;


Select ProductName from Products where InStock ='Yes'
Union
Select ProductName from Products where ProductID In (Select ProductID from orders);

-- Task 2
- Identify products that are both in stock and have been ordered.

Select ProductName from Products where InStock= 'Yes'
Intersect
Select ProductName from Products where ProductID In (Select ProductID from orders);

-- Task 3
-- Find products that are in stock but have never been ordered.

Select ProductName from Products where InStock = 'Yes'
Intersect
Select ProductName from Products where ProductID In (Select ProductID from orders);
