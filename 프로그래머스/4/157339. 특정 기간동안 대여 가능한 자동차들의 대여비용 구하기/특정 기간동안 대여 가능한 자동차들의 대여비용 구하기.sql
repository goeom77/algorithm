-- 코드를 입력하세요
SELECT distinct CRCC.CAR_ID as CAR_ID, CRCC.CAR_TYPE as CAR_TYPE, round((1 - CRCDP.discount_rate/100) * 30 * crcc.daily_fee,0) as FEE
FROM CAR_RENTAL_COMPANY_CAR CRCC 
JOIN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    GROUP BY CAR_ID
    HAVING SUM (
        CASE 
        WHEN (START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01')
        THEN 1
        ELSE 0
    END
    ) = 0

) as CCRH
ON CRCC.CAR_ID = CCRH.CAR_ID
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN CRCDP
ON CRCC.CAR_TYPE = CRCDP.CAR_TYPE
WHERE CRCC.CAR_TYPE IN ('세단','SUV')
and crcdp.duration_type = '30일 이상'
and round((1 - CRCDP.discount_rate/100) * 30 * crcc.daily_fee,0) >= 500000
and round((1 - CRCDP.discount_rate/100) * 30 * crcc.daily_fee,0) < 2000000
order by fee desc, car_type asc, car_id desc