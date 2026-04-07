SELECT
    CASE
        WHEN grade >= 8 THEN name
        ELSE NULL
    END AS name,
    grade,
    marks
FROM students s
LEFT JOIN grades g ON s.marks BETWEEN g.min_mark AND g.max_mark
ORDER BY grade DESC,
    CASE
        WHEN g.grade >= 8 THEN name
        ELSE marks
    END ASC

/*
ORDER BY를 CASE로 해서 가능
*/