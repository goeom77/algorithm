-- 코드를 입력하세요
select book.category, sum(book_sales.sales) as total_sales
from book
join book_sales on book_sales.book_id = book.book_id
where MONTH(book_sales.sales_date) = "01"
group by category
order by category asc