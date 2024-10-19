-- 코드를 입력하세요
select date_format(a.start_date, '%m') month, a.car_id, count(a.car_id) as records
from (
    SELECT car_id, count(car_id) as records
    from car_rental_company_rental_history
    where date_format(start_date, '%m') in (8,9,10)
    group by car_id
    having records >= 5
) b
left join car_rental_company_rental_history a
on a.car_id = b.car_id
where date_format(start_date, '%m') in (8,9,10)
group by date_format(start_date, '%m'), a.car_id
having records > 0
order by month asc, car_id desc