-- 코드를 입력하세요
SELECT
    YEAR(S.SALES_DATE) YEAR,
    MONTH(S.SALES_DATE) MONTH,
    COUNT(DISTINCT S.USER_ID) PUCHASED_USERS,
    ROUND(COUNT(DISTINCT S.USER_ID)/(SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED)=2021) ,1) PUCHASED_RATIO
FROM ONLINE_SALE S
    JOIN USER_INFO I
        ON S.USER_ID = I.USER_ID AND YEAR(I.JOINED)=2021
GROUP BY YEAR, MONTH
ORDER BY YEAR ASC, MONTH ASC
