# Question1: Write the SQL queries to display the total amount earned by each employee's name and surname.
## Answer: 

> SELECT E.FirstName, E.LastName, SUM(P.Value) AS SumAmount 
> FROM Employee E
> JOIN Payments P ON E.EmployeeID = P.EmployeeID
> GROUP BY E.EmployeeID;


# Question 2: Display all employees that have their names starting with the J letter.

## Answer:

> SELECT * FROM Employee WHERE FirstName LIKE 'J%';