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


