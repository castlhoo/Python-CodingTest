SELECT
    N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N IN (
            SELECT b1.N
            FROM bst b1
            LEFT JOIN bst b2 ON b1.N = b2.P
            WHERE b2.P IS NULL
        ) THEN 'Leaf'
    ELSE 'Inner'
    END
FROM bst
ORDER BY N

/*
WHEN N IN 하는게 Key, 그리고 b1.N = b2.P 해서 조인할 때의 어떤 테이블인지 잘 고민해보기 (어떤 테이블인지, 어떤 조인인지,,,어떤 조건)
*/