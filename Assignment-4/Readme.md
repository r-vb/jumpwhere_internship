~~~~sql
-- SQL Basics Assignment -4 Queries

-- 1.
SELECT * FROM Emp WHERE DeptNo = 10 OR DeptNo = 30;

-- 2.
SELECT d.* FROM Dept d
WHERE (SELECT COUNT(*) FROM Emp e WHERE e.DeptNo = d.DeptNo) > 1;

-- 3.
SELECT * FROM Emp WHERE Ename LIKE 'S%';

-- 4.
SELECT * FROM Emp 
WHERE DATEDIFF(YEAR, Hire_Date, GETDATE()) > 2;
-- in SQLite, YEAR isn't working, so..
SELECT * FROM Emp 
WHERE (strftime('%Y', 'now') - strftime('%Y', Hire_Date)) > 2;

-- 5.
SELECT REPLACE(Ename, 'a', '#') AS ModifiedName, * FROM Emp;

-- 6.
SELECT e.Ename AS EmployeeName, m.Ename AS ManagerName
FROM Emp e
LEFT JOIN Emp m ON e.Mgr = m.EmpNo;

-- 7.
SELECT d.Dname, SUM(e.Sal) AS TotalSalary
FROM Dept d
LEFT JOIN Emp e ON d.DeptNo = e.DeptNo
GROUP BY d.Dname;

-- 8.
SELECT e.*, d.Dname, d.Loc
FROM Emp e
RIGHT JOIN Dept d ON e.DeptNo = d.DeptNo;

-- 9.
UPDATE Emp SET Sal = Sal * 1.1;

-- 10.
DELETE FROM Emp
WHERE DeptNo IN (SELECT DeptNo FROM Dept WHERE Loc = 'Chennai');

-- 11.
SELECT Ename, (Sal + COALESCE(Commission, 0)) AS GrossSalary FROM Emp;

-- 12.
ALTER TABLE Emp MODIFY Ename VARCHAR(250);

-- 13.
SELECT GETDATE();
-- 14.
CREATE TABLE STUDENT (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    DateOfBirth DATE,
    Major VARCHAR(50),
    GPA DECIMAL(3,2)
);

-- 15.
SELECT COUNT(*) AS EmployeeCount FROM Emp WHERE Sal > 10000;

-- 16.
SELECT 
    MIN(Sal) AS MinimumSalary,
    MAX(Sal) AS MaximumSalary,
    AVG(Sal) AS AverageSalary
FROM Emp;

-- 17.
SELECT d.Loc, COUNT(e.EmpNo) AS EmployeeCount
FROM Dept d
LEFT JOIN Emp e ON d.DeptNo = e.DeptNo
GROUP BY d.Loc;

-- 18.
SELECT Ename FROM Emp ORDER BY Ename DESC;

-- 19.
CREATE TABLE EMP_BKP AS SELECT * FROM Emp;

-- 20.
SELECT CONCAT(LEFT(Ename, 3), Sal) FROM Emp;

-- 21.
SELECT * FROM Emp WHERE Ename LIKE 'S%';

-- 22.
SELECT e.* 
FROM Emp e
JOIN Dept d ON e.DeptNo = d.DeptNo
WHERE d.Loc = 'Bangalore';

-- 23.
SELECT * FROM Emp WHERE Ename >= 'A' AND Ename < 'L';

-- 24.
SELECT e.* 
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo
WHERE m.Ename = 'Stefen';

-- 25.
SELECT m.Ename, COUNT(e.EmpNo) AS EmployeeCount
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo
GROUP BY m.Ename
HAVING COUNT(e.EmpNo) = (
    SELECT MAX(EmployeeCount)
    FROM (
        SELECT COUNT(e2.EmpNo) AS EmployeeCount
        FROM Emp e2
        WHERE e2.Mgr IS NOT NULL
        GROUP BY e2.Mgr
    ) AS ManagerCounts
);

-- 26.
SELECT e.*, d.*, m.*
FROM Emp e
JOIN Dept d ON e.DeptNo = d.DeptNo
JOIN Emp m ON e.Mgr = m.EmpNo
WHERE e.Sal = (
    SELECT MAX(Sal)
    FROM Emp
    WHERE Sal < (SELECT MAX(Sal) FROM Emp)
);

-- 27.
SELECT DISTINCT m.*
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo;

-- 28.
SELECT DISTINCT m.*, DATEDIFF(YEAR, m.Hire_Date, GETDATE()) AS Experience
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo;

-- 29.
SELECT DISTINCT m.*
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo
JOIN Dept d ON m.DeptNo = d.DeptNo
WHERE m.Commission < 1000
AND d.Loc = 'Delhi';

-- 30.
SELECT e.*
FROM Emp e, Emp martin
WHERE martin.Ename = 'Martin'
AND e.Hire_Date < martin.Hire_Date;
~~~~
