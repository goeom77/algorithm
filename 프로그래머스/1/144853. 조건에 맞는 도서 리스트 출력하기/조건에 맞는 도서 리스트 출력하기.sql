-- 코드를 입력하세요
SELECT BOOK_ID,
SUBSTRING(PUBLISHED_DATE,1,10) AS PUBLISHED_DATE
FROM BOOK
WHERE SUBSTRING(PUBLISHED_DATE,1,4) = 2021 AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE ASC