CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(255),
    commission DECIMAL(4, 2)
);


SELECT * FROM salesman;

INSERT INTO salesman (salesman_id, name, city, commission) VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5003, 'Lauson Hen', NULL, 0.12),
(5007, 'Paul Adam', 'Rome', 0.13);


-- Task 1
-- Find the average commision of salesman from Paris
SELECT AVG(commission) AS average_commission
FROM salesman
WHERE city = 'Paris';

-- Task 2
-- Find out if there are cities with only one salesman and list them
SELECT city
FROM salesman
GROUP BY city
HAVING COUNT(*) = 1;

--Task 3
--3.1 Determine the maximum commission in each city
select city, max(commission)
from salesman 
where city is not null  
group by city ;
--3.2 list the salesman who earn this commission
--Clue: Join



CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);
 
 
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
(70001, 150.5, '2012-10-05', 3005, 5002),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70002, 65.26, '2012-10-05', 3002, 5001),
(70004, 110.5, '2012-08-17', 3009, 5003),
(70007, 948.5, '2012-09-10', 3005, 5002),
(70005, 2400.6, '2012-07-27', 3007, 5001),
(70008, 5760, '2012-09-10', 3002, 5001),
(70010, 1983.43, '2012-10-10', 3004, 5006),
(70003, 2480.4, '2012-10-10', 3009, 5003),
(70012, 250.45, '2012-06-27', 3008, 5002),
(70011, 75.29, '2012-08-17', 3003, 5007),
(70013, 3045.6, '2012-04-25', 3002, 5001);

select * from orders;

-- Task 4 - Sub-Query
-- Write a query to display all the orders from the order table issued by the salesman 'Paul Adam'.
Select *
from orders
Join salesman
On orders.salesman_id = salesman.salesman_id
Where name = 'Paul Adam';


-- Task 5 
-- Write a query to display all the orders which values are greater than the average order value for 10th October 2012
SELECT *
FROM orders
WHERE purch_amt > (
    SELECT AVG(purch_amt) 
    FROM orders 
    WHERE ord_date = '2012-10-10'
);


-- Task 6
-- Write a query to find all orders with order amounts which are above-average amounts for their customers.

Select * 
from orders
Where purch_amt > (
	SELECT AVG(purch_amt)
    FROM orders 
    WHERE customer_id = customer_id
);





