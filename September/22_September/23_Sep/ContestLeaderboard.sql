SELECT
    h.hacker_id,
    h.name,
    SUM(c.best_score) AS total_score
FROM hackers h
LEFT JOIN (
    SELECT
        hacker_id,
        challenge_id,
        MAX(score) AS best_score
    FROM submissions
    GROUP BY hacker_id, challenge_id
) c
    ON c.hacker_id = h.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total_score > 0
ORDER BY total_score DESC, hacker_id ASC