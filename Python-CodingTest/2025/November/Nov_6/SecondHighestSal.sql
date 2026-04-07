-- Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

-- The result format is in the following example.

WITH rank_table AS (
    SELECT
        id,
        salary,
        RANK() OVER(ORDER BY salary DESC) AS sal_rank
    FROM Employee
)
SELECT 
    COALESCE((
        SELECT salary 
        FROM rank_table 
        WHERE sal_rank = 2
        LIMIT 1
    ), NULL) AS SecondHighestSalary;
