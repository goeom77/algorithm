-- 코드를 입력하세요
WITH RECURSIVE cte AS (
    SELECT 0 AS num
    UNION ALL
    SELECT num+1
    FROM cte
    WHERE num < 23
)

SELECT cte.num AS HOUR, IFNULL(a.입양횟수, 0) AS COUNT
FROM cte
LEFT JOIN (SELECT HOUR(datetime) 시간대, COUNT(*) 입양횟수
           FROM animal_outs
           GROUP BY 시간대
           ) a
ON cte.num = a.시간대;