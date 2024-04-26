# SQL Queries:
 
 [SQLBolt](https://sqlbolt.com/): A series of interactive lessons and exercises designed to help you quickly learn SQL right in your browser.

 ## Exercise 1 — Select Queries

1. Find the title of each film 

    ```SELECT Title from movies;```

2. Find the director of each film 

    ```Select Director from movies;```

3. Find the title and director of each film

    ```Select Title,director from movies;```

4. Find the title and year of each film

    ```Select Title,year from movies;```

5. Find all the information about each film

    ```Select * from movies;```

## Exercise 2 - Queries with constraints

1. Find the movie with a row id of 6

    ```SELECT * FROM Movies where id = 6;```

2. Find the movies released in the years between 2000 and 2010

    ```Select * from Movies where Year between 2000 and 2010;```

3. Find the movies not released in the years between 2000 and 2010

    ```Select * from Movies where Year not between 2000 and 2010;```

4. Find the first 5 Pixar movies and their release year

    ```SELECT * FROM movies where id <= 5;```

## Exercise 3 - Queries with constraints

1. Find all the Toy Story movies

    ``` 
    SELECT * FROM Movies
    WHERE Title LIKE 'Toy Story%';
    ```

2. Find all the movies directed by John Lasseter

    ```
    SELECT * FROM Movies
    WHERE Director LIKE 'John Lasseter%';
    ```

3. Find all the movies (and director) not directed by John Lasseter

    ```
    SELECT * FROM Movies
    WHERE Director NOT LIKE 'John Lasseter%';
    ```

4. Find all the WALL-* movies

    ```
    SELECT * FROM Movies
    WHERE Title LIKE 'Wall%';
    ```

## Exercise 4 - Filtering and sorting Query results

1. List all directors of Pixar movies (alphabetically), without duplicates

    ```
    SELECT DISTINCT Director FROM movies
    Order by Director ASC;
    ```

2. List the last four Pixar movies released (ordered from most recent to least)

    ```
    SELECT * FROM movies
    Order by Year DESC
    Limit 4;
    ```
3. List the first five Pixar movies sorted alphabetically

    ```
    SELECT * FROM movies
    ORDER BY Title ASC
    LIMIT 5;
    ```

4. List the next five Pixar movies sorted alphabetically

    ```
    SELECT * FROM movies
    ORDER BY Title ASC
    LIMIT 5 OFFSET 5;
    ```

    ## SQL Review: Simple SELECT Queries

    ### Review 1 — Tasks
1. List all the Canadian cities and their populations

    ```
    SELECT City, Population
    FROM North_american_cities
    WHERE Country = 'Canada';
    ```
2. Order all the cities in the United States by their latitude from north to south

    ```
    SELECT City FROM north_american_cities
    Where Country = 'United States'
    ORDER BY Latitude DESC;
    ```
3. List all the cities west of Chicago, ordered from west to east

    ```
    SELECT * FROM north_american_cities
    ORDER BY longitude limit 6;
    ```
4. List the two largest cities in Mexico (by population)

    ```
    SELECT City FROM north_american_cities
    Where Country = 'Mexico'
    Order by population DESC
    limit 2;
    ```

5. List the third and fourth largest cities (by population) in the United States and their population

    ```
    SELECT City FROM north_american_cities
    WHERE Country = 'United States'
    ORDER BY Population DESC
    limit 2 offset 2;
    ```

## SQL Lesson 6: Multi-table queries with JOINs

1. Find the domestic and international sales for each movie

    ```
    SELECT Title, Domestic_sales, International_sales
    FROM Movies
    JOIN Boxoffice
    ON Movies.id = boxoffice.Movie_id;
    ```

2. Show the sales numbers for each movie that did better internationally rather than domestically

    ```
    select title, domestic_sales, international_sales
    from movies
    join boxoffice
    on movies.id = boxoffice.movie_id
    where domestic_sales < international_sales;
    ```

3. List all the movies by their ratings in descending order

    ```
    Select *
    from movies
    join boxoffice
    on boxoffice.movie_id = movies.id
    order by rating DESC;
    ```

## SQL Lesson 7: OUTER JOINs

1. Find the list of all buildings that have employees 

    ```
    SELECT DISTINCT building 
    FROM employees;
    ```

2. Find the list of all buildings and their capacity

    ```
    SELECT * FROM buildings;
    ```

3. List all buildings and the distinct employee roles in each building (including empty buildings)

    ```
    Select distinct Building_name, role 
    from Buildings
    Left Join Employees
    ON Buildings.Building_name = Employees.Building;
    ```

## SQL Lesson 8: A short note on NULLs

1. Find the name and role of all employees who have not been assigned to a building

    ```
    SELECT name, role 
    FROM employees
    WHERE Building IS NULL;
    ```

2. Find the names of the buildings that hold no employees

    ```
    SELECT Building_name 
    FROM Buildings
    LEFT JOIN Employees
    ON Building_name = building
    WHERE Building IS NULL;
    ```

## SQL Lesson 9: Queries with expressions

1. List all movies and their combined sales in millions of dollars

    ```
    SELECT title, (domestic_sales + international_sales) / 1000000 AS gross_sales_millions
    FROM movies
    JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
    ```

2. List all movies and their ratings in percent

    ```
    SELECT title, rating * 10 AS rating_percent
    FROM movies
    JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
    ```

3. List all movies that were released on even number years

    ```
    SELECT title, year
    FROM movies
    WHERE year % 2 = 0;
    ```
## SQL Lesson 10: Queries with aggregates (Pt. 1)

1. Find the longest time that an employee has been at the studio

    ```
    SELECT *, Max(Years_employed) from employees;
    ```

2. For each role, find the average number of years employed by employees in that role

    ```
    SELECT Role, AVG(Years_employed) AS Average_Years_Employed
    FROM employees
    Group by Role;
    ```

3. Find the total number of employee years worked in each building

    ```
    SELECT building, SUM(years_employed) as Total_years_employed
    FROM employees
    GROUP BY building;
    ```

## SQL Lesson 11: Queries with aggregates (Pt. 2)

1. Find the number of Artists in the studio (without a HAVING clause)

    ```
    SELECT Role, Count(Role) 
    FROM employees
    WHERE Role = 'Artist';
    ```

2. Find the number of Employees of each role in the studio

    ```
    SELECT role, COUNT(*)
    FROM employees
    GROUP BY role;
    ```

3. Find the total number of years employed by all Engineers

    ```
    SELECT Role, SUM(Years_employed)
    FROM employees
    WHERE Role = 'Engineer';
    ```

## SQL Lesson 12: Order of execution of a Query

### Exercise 12 — Tasks
1. Find the number of movies each director has directed

    ```
    SELECT director, COUNT(id) as No_of_movies_directed
    FROM movies
    GROUP BY director;  
    ```

2. Find the total domestic and international sales that can be attributed to each director

    ```
    SELECT Director, SUM(Domestic_sales + International_sales)
    FROM movies
    JOIN Boxoffice
    On Movies.id = Boxoffice.movie_id
    GROUP BY director;
    ```
## SQL Lesson 13: Inserting rows

### Exercise 13 — Tasks
1. Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)

    ```
    INSERT INTO movies VALUES (15, "Toy Story 4", "Samar", 2025, 190);
    ```

2. Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.

    ```
    Insert into Boxoffice
    Values(15, 8.7, 340000000, 270000000);
    ```

## SQL Lesson 14: Updating rows

>Tip: Use SELECT query to filter the specific rows, then UPDATE.

### Exercise 14 — Tasks
1. The director for A Bug's Life is incorrect, it was actually directed by John Lasseter

    ```
    UPDATE movies
    SET director = "John Lasseter"
    WHERE id = 2;
    ```

2. The year that Toy Story 2 was released is incorrect, it was actually released in 1999

    ```
    UPDATE movies
    SET year = 1999
    WHERE id = 3;
    ```

3. Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich

    ```
    UPDATE movies
    SET title = "Toy Story 3", director = "Lee Unkrich"
    WHERE id = 11;
    ```

## SQL Lesson 15: Deleting rows

### Exercise 15 — Tasks
1. This database is getting too big, lets remove all movies that were released before 2005.

    ```
    DELETE FROM movies
    where year < 2005;
    ```

2. Andrew Stanton has also left the studio, so please remove all movies directed by him.

    ```
    DELETE FROM movies
    Where Director = "Andrew Stanton";
    ```

## SQL Lesson 16: Creating tables

DataTypes : FLOAT - 3, Double - 6, REAL - 12

### Exercise 16 — Tasks

1. Create a new table named Database with the following columns:
– Name A string (text) describing the name of the database
– Version A number (floating point) of the latest version of this database
– Download_count An integer count of the number of times this database was downloaded
This table has no constraints.

    ```
    CREATE TABLE Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER
    );
    ```

## SQL Lesson 17: Altering tables

### Exercise 17 — Tasks
1. Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in. 

    ```
    ALTER TABLE Movies
    ADD COLUMN Aspect_ratio FLOAT DEFAULT 2.39;
    ```

2. Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.

    ```
    ALTER TABLE Movies
    ADD COLUMN Language TEXT DEFAULT "English";
    ```

## SQL Lesson 18: Dropping tables

### Exercise 18 — Tasks
1. We've sadly reached the end of our lessons, lets clean up by removing the Movies table

    ```
    DROP TABLE Movies;
    ```

2. And drop the BoxOffice table as well

    ```
    DROP TABLE BoxOffice;
    ```


