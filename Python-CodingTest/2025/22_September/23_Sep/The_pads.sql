SELECT result
FROM( 
    SELECT
        CONCAT(name,'(',SUBSTR(occupation,1,1),')') AS result,
        1 as ord,
        name as k1,
        NULL as k2,
        NULL as k3
        
    FROM occupations

    UNION ALL

    SELECT 
        CONCAT('There are a total of ', COUNT(*),' ',LOWER(occupation),'s.') AS result,
        2 as ord,
        NULL as k1,
        COUNT(*) as k2,
        LOWER(occupation) as k3
    FROM occupations
    GROUP BY occupation
) x
ORDER BY ord,k1,k2,k3


/* Neet to memorize
- 1. SUBSTR(target, start, last)
- 2. If we need to order by multiple options, need to consider about making multiple elements for ordering.