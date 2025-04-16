--  authors that viewed at least one of their own articles

# Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM views
WHERE author_id = viewer_id
GROUP BY article_id
ORDER BY id ASC