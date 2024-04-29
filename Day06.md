## Agenda - 29/04/24

1. Equi, Natural, Inner Join
2. Sub Queries -> Exists, Not Exists
3. Union, Intersection, Except
4. Limit, Offset -> MS SQL
5. Types of Keys, ACID (Theory Part)
6. Group By, Order By -> Advanced

[SQL Document by Microsoft](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver16)

### Different Types of Keys:

1. Candidate Key - Any key that is can be a contender to become a primary key, which have potential (Unique & Not Null) to be primary key.
  [Candidate Key = Primary Key U Alternate Key]
2. Super Key - Combination of keys (Primary Key + Candidate Key + Alternate Key) that uniquely identifies a record.
3. Difference btw Super Key & Composite Key: In SQL, a super key is a set of one or more attributes (columns) that uniquely identifies a tuple (row) in a relation (table). A composite key, on the other hand, is a specific type of super key consisting of multiple attributes combined to uniquely identify a tuple. So, a composite key is a type of super key, but not all super keys are composite keys.

### ACID Properties:

A Good database is identified by ACID properties.
1. A - Atomicity -> (All or Nothing) -> Success or Failure
2. C - Consistency
3. I - Isolation
4. D - Durability

> NOSQL is BASE
