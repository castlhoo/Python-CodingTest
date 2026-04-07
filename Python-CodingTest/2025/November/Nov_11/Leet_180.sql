-- 180. Consecutive Numbers
-- Solved
-- Medium
-- Topics
-- premium lock icon
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Logs

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- In SQL, id is the primary key for this table.
-- id is an autoincrement column starting from 1.
 

-- Find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

-- The result format is in the following example.

WITH CTE AS (
    SELECT
        id,
        num,
        LAG(num, 1) OVER (ORDER BY id) AS previous_1,
        LAG(num, 2) OVER (ORDER BY id) AS previous_2
    FROM logs
)
SELECT DISTINCT
    num AS ConsecutiveNums
FROM CTE
WHERE num = previous_1 AND num = previous_2;
