CREATE DATABASE EmployeeDB;

CREATE TABLE Department(
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

CREATE TABLE Employee(
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(50),
    Salary DECIMAL(10,2),
    DepartmentID INT,
    FOREIGN KEY(DepartmentID) REFERENCES Department(DepartmentID)
);

INSERT INTO Department VALUES
(1,'HR'),
(2,'IT'),
(3,'Finance'),
(4,'Marketing');

INSERT INTO Employee VALUES
(101,'Rahul',45000,1),
(102,'Prakash',60000,2),
(103,'Anil',55000,3),
(104,'Kiran',75000,2),
(105,'Ravi',40000,4),
(106,'Arun',65000,3);

SELECT * FROM Employee;

SELECT DISTINCT DepartmentName FROM Department;

SELECT EmployeeID,EmployeeName,Salary FROM Employee WHERE Salary>50000;

SELECT e.EmployeeName,d.DepartmentName
FROM Employee e
INNER JOIN Department d ON e.DepartmentID=d.DepartmentID
WHERE d.DepartmentName='IT';

SELECT EmployeeName,Salary FROM Employee WHERE Salary BETWEEN 40000 AND 60000;

SELECT e.EmployeeName,d.DepartmentName
FROM Employee e
INNER JOIN Department d ON e.DepartmentID=d.DepartmentID
WHERE d.DepartmentName IN('IT','Finance');

SELECT EmployeeName,Salary FROM Employee ORDER BY Salary DESC;

SELECT e.EmployeeName,e.Salary,d.DepartmentName
FROM Employee e
INNER JOIN Department d ON e.DepartmentID=d.DepartmentID
WHERE e.Salary>50000 AND d.DepartmentName='IT';

SELECT e.EmployeeName,d.DepartmentName
FROM Employee e
INNER JOIN Department d ON e.DepartmentID=d.DepartmentID
WHERE d.DepartmentName='HR' OR d.DepartmentName='Finance';

SELECT e.EmployeeName,d.DepartmentName
FROM Employee e
INNER JOIN Department d ON e.DepartmentID=d.DepartmentID
WHERE NOT d.DepartmentName='IT';