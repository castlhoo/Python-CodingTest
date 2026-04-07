-- -- 1045. Customers Who Bought All Products
-- -- Solved
-- -- Medium
-- -- Topics
-- -- premium lock icon
-- -- Companies
-- -- SQL Schema
-- -- Pandas Schema
-- -- Table: Customer

-- -- +-------------+---------+
-- -- | Column Name | Type    |
-- -- +-------------+---------+
-- -- | customer_id | int     |
-- -- | product_key | int     |
-- -- +-------------+---------+
-- -- This table may contain duplicates rows. 
-- -- customer_id is not NULL.
-- -- product_key is a foreign key (reference column) to Product table.
 

-- -- Table: Product

-- -- +-------------+---------+
-- -- | Column Name | Type    |
-- -- +-------------+---------+
-- -- | product_key | int     |
-- -- +-------------+---------+
-- -- product_key is the primary key (column with unique values) for this table.
 

-- -- Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.

-- -- Return the result table in any order.

-- -- The result format is in the following example.

 

-- -- Example 1:

-- -- Input: 
-- -- Customer table:
-- -- +-------------+-------------+
-- -- | customer_id | product_key |
-- -- +-------------+-------------+
-- -- | 1           | 5           |
-- -- | 2           | 6           |
-- -- | 3           | 5           |
-- -- | 3           | 6           |
-- -- | 1           | 6           |
-- -- +-------------+-------------+
-- -- Product table:
-- -- +-------------+
-- -- | product_key |
-- -- +-------------+
-- -- | 5           |
-- -- | 6           |
-- -- +-------------+
-- -- Output: 
-- -- +-------------+
-- -- | customer_id |
-- -- +-------------+
-- -- | 1           |
-- -- | 3           |
-- -- +-------------+
-- -- Explanation: 
-- -- The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.

-- # Write your MySQL query statement below
-- SELECT
--     customer_id
-- FROM customer c
-- GROUP BY customer_id
-- HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM product)

-- # Write your MySQL query statement below
WITH CTE AS(
    SELECT
        product_id,
        MAX(change_date) AS sol_date
    FROM products
    WHERE change_date <= "2019-08-16"
    GROUP BY product_id
)

SELECT
    p.product_id, 
    CASE WHEN new_price IS NULL THEN 10 ELSE new_price END AS price
FROM products p
INNER JOIN CTE c ON p.change_date = c.sol_date AND p.product_id = c.product_id

UNION

SELECT
    DISTINCT product_id,
    10 AS price
FROM products
WHERE product_id NOT IN(
    SELECT product_id
    FROM products
    WHERE change_date <= "2019-08-16"
)