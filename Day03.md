# Introduction to Database:

### What is a Database?
- Special software to store data.
- A database (DB) is an organized collection of data. 

### Where does databases live?
- Cloud - Renting PCs.
    - Egs: AWS, Azure, GCP, IBM Cloud, Salesforce.
- Renting is best than buying  because you don't have to maintain it.
- Provides Disaster Management.
- Auto Scaling.
    - Possibily of DDoS attacks: 

### OS used in Cloud -> [ Linux ] -> (DevOps People will use.)
- Free
- Open Source
- Secure
- Small footprint
- Automation
- Performace
- Lots of flavours (distros)
    - Ubuntu
    - Archlinux
    - debian
    - fedora
    - kali linux
    - Alphine linux (smallest footprint among  all distros - 256mb)

### Why Database?
    - frequently asked it will have it in the ram.
    - querying become easier
    - CRUD - easy
    - Backups are inbuilt
    - UNdo - easily (time limit)
    - Performance (By using indexing)

### Database Types:
    1. SQL - Structured data.
        - Examples: MySQL, PostgreSQL, PL/SQL, Amazon RDS
    2. NoSQL - Semi Structured data.
        - Examples: MongoDB, Redis, CouchDB, Cassandra, DynamoDB

### Queries:
 
> [SQLBolt](https://sqlbolt.com/): A series of interactive lessons and exercises designed to help you quickly learn SQL right in your browser.

### Normalization
- Improving safety 
- Avoid Anomaly
- As level increasing it gets more safer.
- Reduce the risk
- Removing duplicate data (Which increases Safety).

# Normalization in Databases

## What is Normalization?
Normalization is a process used in database design to organize data efficiently, reduce redundancy, and ensure data integrity. It involves breaking down a large table into smaller, more manageable tables and establishing relationships between them. Normalization helps in eliminating data anomalies and ensures that the database structure adheres to certain rules.

## Why Normalization?
Normalization is essential for several reasons:
- Reduces data redundancy
- Minimizes update anomalies
- Improves data integrity
- Enhances database performance
- Facilitates easier database maintenance and management

### Keywords:

- **Primary Key**: A unique identifier for each record in a table.
  - Example: Student_ID in a table of students.
  
- **Composite Primary Key**: A primary key that consists of more than one attribute.
  - Example: {Order_ID, Product_ID} in a table of orders and products.

- **Foreign Key**: A column in one table that references the primary key in another table.
  - Example: Department_ID in a table of employees, referencing the Department_ID in a table of departments.

- **Functional Dependency**: When knowing the value of one attribute determines the value of another attribute.
  - Example: Knowing the Social Security Number (SSN) of a person determines their Name.

- **Transitive Dependency**: When one non-key attribute determines another non-key attribute indirectly through a third attribute.
  - Example: In a table where City determines State, and State determines Country, City → State → Country is a transitive dependency.

- **Indirect Dependency**: Similar to transitive dependency, it refers to a situation where one attribute depends on another, which, in turn, depends on a third attribute.
  - Example: If a customer's Address depends on the Location, and the Location depends on the ZIP code, then Address → Location → ZIP code is an indirect dependency.

- **Candidate Key**: A minimal set of attributes that uniquely identify each tuple in a relation.
  - Example: {Student_ID} or {Email} can be candidate keys in a table of students.

- **Atomic Value**: A value that cannot be divided further.
  - Example: A cell in a table containing a single value like "John Smith" or "123 Main Street".

- **Partial Dependency**: When non-key attributes are dependent on only part of the primary key.
  - Example: In a table where {Student_ID, Course} → Grade, if Grade depends only on Course, it's a partial dependency.

- **Normalization**: The process of organizing data in a database to reduce redundancy and improve data integrity. (safety)
  - Example: Splitting a single table with customer information into separate tables for customers and their orders to avoid duplicating customer data.

- **Denormalization**: The process of intentionally adding redundancy to a database for performance reasons.
  - Example: Storing calculated values, like total order amount, in a table to avoid having to calculate them each time they're needed.

- **Anomaly**: An error or inconsistency in the data that occurs due to improper database design.
  - Example: Insertion, update, or deletion anomalies that arise when a database table is not properly normalized.

- **Dependency**: A relationship between attributes in a database, where the value of one attribute determines the value of another.
  - Example: The value of a Customer_ID attribute determines the corresponding customer's Name and Address.

## Normalization Forms
### 1. First Normal Form (1NF)
- **What**: Ensures that each column in the table contains atomic (indivisible) values.
- **Why**: Avoids repeating groups and ensures data integrity.
- **How**: Splitting multi-valued attributes into separate columns or rows.

      - Don't use row order to convey info.
      - Keep data types consistent.
      - Every row needs a unique identifier (Primary Key).
      - Don't repeat groups of data.

**Example**:

**Incorrect Table (1NF)**:

| Band_Name   | Members              |
|-------------|----------------------|
| Beatles     | Paul, John, George, Ringo |

**Incorrect Table Explanation**: In the incorrect table, the "Members" column violates 1NF by storing multiple member names in a single cell.

**Correct Table (1NF)**:

| Band_Name   | Member       |
|-------------|--------------|
| Beatles     | Paul         |
| Beatles     | John         |
| Beatles     | George       |
| Beatles     | Ringo        |

**Correct Table Explanation (1NF)**: The corrected table splits the multi-valued attribute "Members" into separate rows, ensuring atomic values in each cell.

### 2. Second Normal Form (2NF)
- **What**: Ensures that all non-key attributes are fully functionally dependent on the primary key.
- **Why**: Eliminates partial dependencies and improves data integrity.
- **How**: Splitting tables to remove partial dependencies.

      - Follow 1NF.
      - Have a special key made from more than one part (Composite Primary Key).
      - Everything else should depend fully on that key.

**Example**:

**Incorrect Table (2NF)**:

| Band_Name   | Member       | Role           |
|-------------|--------------|----------------|
| Beatles     | Paul         | Lead Singer    |
| Beatles     | John         | Guitarist      |
| Beatles     | George       | Guitarist      |
| Beatles     | Ringo        | Drummer        |

**Incorrect Table Explanation**: In the incorrect table, the "Role" attribute depends on the "Band_Name," which is part of the composite primary key, creating partial dependencies.

**Correct Tables (2NF)**:

| Band_Name   | Member       |
|-------------|--------------|
| Beatles     | Paul         |
| Beatles     | John         |
| Beatles     | George       |
| Beatles     | Ringo        |

| Member       | Role           |
|--------------|----------------|
| Paul         | Lead Singer    |
| John         | Guitarist      |
| George       | Guitarist      |
| Ringo        | Drummer        |

**Correct Tables Explanation (2NF)**: We split the original table into two separate tables to remove partial dependencies. Each table now has a single primary key, and all non-key attributes are fully functionally dependent on it.

### 3. Third Normal Form (3NF)
- **What**: Ensures that there are no transitive dependencies between non-key attributes.
- **Why**: Removes transitive dependencies and improves data integrity.
- **How**: Further splitting tables to eliminate transitive dependencies.

      - Meet 2NF.
      - No indirect dependencies between non-key items.

**Example**:

**Incorrect Table (3NF)**:

| Member       | Role           | Band_Name   |
|--------------|----------------|-------------|
| Paul         | Lead Singer    | Beatles     |
| John         | Guitarist      | Beatles     |
| George       | Guitarist      | Beatles     |
| Ringo        | Drummer        | Beatles     |

**Incorrect Table Explanation**: In the incorrect table, "Band_Name" depends on "Member," which is not a primary key, creating a transitive dependency.

**Correct Tables (3NF)**:

| Member_ID | Member       | Band_ID |
|-----------|--------------|---------|
| 1         | Paul         | 1       |
| 2         | John         | 1       |
| 3         | George       | 1       |
| 4         | Ringo        | 1       |

| Band_ID | Band_Name   |
|---------|-------------|
| 1       | Beatles     |

| Role_ID | Role         |
|---------|--------------|
| 1       | Lead Singer  |
| 2       | Guitarist    |
| 3       | Drummer      |

**Correct Tables Explanation (3NF)**: We further normalize the data by splitting attributes into multiple tables to remove transitive dependencies. Each table represents a distinct entity, and there are no transitive dependencies between non-key attributes.

### 4. Boyce-Codd Normal Form (BCNF)
- **What**: Ensures that every determinant is a candidate key.
- **Why**: Eliminates non-trivial functional dependencies.
- **How**: Decomposing tables until each satisfies the criteria for BCNF.

      - Satisfy 3NF.
      - Every reason (determinant) for something must be a potential Primary Key (Candidate Key).

**Example**:

**Incorrect Table (BCNF)**:

| Member       | Role           |
|--------------|----------------|
| Paul         | Lead Singer    |
| John         | Guitarist      |
| George       | Guitarist      |
| Ringo        | Drummer        |

**Incorrect Table Explanation**: In the incorrect table, both "Member" and "Role" are candidate keys, but they determine each other, creating non-trivial functional dependencies.

**Correct Tables (BCNF)**:

| Member_ID | Member       | Role_ID |
|-----------|--------------|---------|
| 1         | Paul         | 1       |
| 2         | John         | 2       |
| 3         | George       | 2       |
| 4         | Ringo        | 3       |

| Role_ID | Role         |
|---------|--------------|
| 1       | Lead Singer  |
| 2       | Guitarist    |
| 3       | Drummer      |

**Correct Tables Explanation (BCNF)**: We introduce surrogate keys ("Member_ID" and "Role_ID") to ensure each table has a single candidate key. Now, each determinant uniquely identifies the attributes, adhering to BCNF.

This explanation provides an overview of each normalization form, including examples of incorrect and correct tables for each, along with explanations of what was wrong and how it was corrected.


------------------------------


## Examples

### 1 NF

![WhatsApp Image 2024-04-24 at 17 06 55_802f1f38](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/02ba9231-06d9-47bf-845c-8b3fdd30b9e6)

#### Analysis of the Problem:
- The given data represents player inventories with Player_ID and their corresponding Inventory items.
- The Inventory column contains multiple items for each player, separated by commas.
- This violates the rules of First Normal Form (1NF), which requires atomic (indivisible) values in each cell and prohibits repeating groups within a row.

#### Action Plan:
1. **Identify Repeating Groups:** Recognize that the Inventory column contains repeating groups of items for each player.
2. **Break Down Repeating Groups:** Separate each item in the Inventory column into its own row, ensuring atomicity.
3. **Normalize the Data:** Reorganize the data into a tabular format where each row represents a single item for a player.

#### Updated Table
![WhatsApp Image 2024-04-24 at 17 06 56_e55e0c30](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/81adaaeb-4e21-451b-b235-2a438aa03d0e)
![WhatsApp Image 2024-04-24 at 17 06 56_37f8368d](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/23f59ff5-dccf-4514-b582-96660c0cf90a)

#### Conclusion (1NF):
- By breaking down the repeating groups and organizing the data into separate rows for each item, we have successfully transformed the data into First Normal Form (1NF).
- Each row now represents a single item in the player's inventory, adhering to the rules of 1NF.

<br>
  
### 2 NF

![WhatsApp Image 2024-04-24 at 16 34 38_d03e5495](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/88a393af-5dbb-4536-a4be-fce36ed59058)

#### Problem Analysis:

1. **Partial Dependency**: In the "Player_Inventory" table, the attribute "Player_Rating" appears to depend only on the "Player_ID" attribute, not on the entire primary key (Player_ID, Item_Type). This creates a partial dependency, violating the requirements of 2NF.

#### Action Plan:

To resolve the partial dependency issue and ensure compliance with 2NF, we need to:

1. **Identify Primary Key**: Confirm the primary key of the table. In this case, it seems to be (Player_ID, Item_Type), as each combination uniquely identifies a row.

2. **Review Non-Prime Attributes**: Examine non-prime attributes (attributes not part of the primary key) to ensure they are fully functionally dependent on the entire primary key.

3. **Separate Partially Dependent Attribute**: Since "Player_Rating" depends only on "Player_ID" and not on the entire primary key, we need to extract it into a separate table where it can be fully functionally dependent on "Player_ID."

#### Updated Tables:

![WhatsApp Image 2024-04-24 at 16 34 38_70c277ae](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/595921fd-d94b-414e-b142-2e131aa018bf)

#### Conclusion:

By separating the "Player_Rating" attribute into its own table, where "Player_ID" serves as the primary key, we have resolved the partial dependency issue and ensured compliance with 2NF. This restructuring enhances data integrity and avoids anomalies in the database.

<br>

### 3 NF

![WhatsApp Image 2024-04-24 at 16 50 51_0b0c4dde](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/13c66256-cdab-422e-88e7-676f8b11be3a)

#### Analysis:

1. **Functional Dependencies**: 
    - Player_ID → Player_Rating (Partial Dependency)
    - Player_ID → Player_Skill_Level (Partial Dependency)

2. **Primary Key**:
    - The primary key of the Player table is {Player_ID}.

3. **Non-Prime Attributes**:
    - Both Player_Rating and Player_Skill_Level are non-prime attributes.

#### Action Plan:

To achieve 3NF, we need to:
1. **Resolve Partial Dependencies**:
    - Separate the non-prime attributes Player_Rating and Player_Skill_Level into their own tables to eliminate partial dependencies.

2. **Create Relationships**:
    - Create relationships between the Player table and the new tables for Player_Rating and Player_Skill_Level.

#### Updated Tables:

![WhatsApp Image 2024-04-24 at 16 48 53_482cc858](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/fc7d4e30-048e-4d6e-80d4-675fa30c4352)

#### Conclusion:
By separating the non-prime attributes into their own tables and ensuring that each table has a single primary key, we have achieved 3NF. This normalization process eliminates partial dependencies and improves the integrity and structure of the database.

<br>

### Boyce-Codd Normal Form (BCNF)

BCNF is a higher level of normalization than 3NF. A table is in BCNF if, for every non-trivial functional dependency \( X \rightarrow Y \):
- \( X \) is a superkey
- There are no non-trivial functional dependencies of the form \( A \rightarrow B \) where \( A \) is a proper subset of \( X \)

A non-trivial functional dependency is one in which \( Y \) is not a subset of \( X \), and a superkey is a set of attributes that uniquely identifies each row in a table.

#### Analysis:

1. **Functional Dependencies**:
    - Player_ID → Player_Rating (Partial Dependency)
    - Player_ID → Player_Skill_Level (Partial Dependency)
    - Skill_Level → Rating (Trivial Dependency)

2. **Primary Keys**:
    - The primary key of the Player table is {Player_ID}.
    - The primary key of the Skill_Level table is {Skill_Level}.

#### Action Plan:

To achieve BCNF, we need to:
1. **Resolve Partial Dependencies**:
    - Separate the non-prime attributes Player_Rating and Player_Skill_Level into their own tables to eliminate partial dependencies.

2. **Ensure Functional Dependency Preservation**:
    - Check if the tables preserve all functional dependencies after decomposition.

#### Updated Tables:

![WhatsApp Image 2024-04-24 at 16 48 53_c2eb9d37](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/6d5630fd-f8b4-4d91-b6f8-47114187262e)
`non key` -> `BCNF`

#### Conclusion:

The provided tables do not satisfy BCNF due to partial dependencies. To achieve BCNF, we need to decompose the tables to eliminate partial dependencies and ensure that each table complies with BCNF requirements.





