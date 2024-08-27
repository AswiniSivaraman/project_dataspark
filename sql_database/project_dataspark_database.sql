create database project_dataspark;

use project_dataspark;

select * from customers;
select * from sales;
select * from store;
select * from products;
select * from exchange_rates;

-- ------------------------------------------------------------ Customer ----------------------------------------------------------------------------------------------------
select gender,count(gender) as gender_count from customers group by gender;

select 
    case 
        when age between 18 and 24 then '18-24'
        when age between 25 and 34 then '25-34'
        when age between 35 and 44 then '35-44'
        when age between 45 and 54 then '45-54'
        when age between 55 and 64 then '55-64'
        when age between 65 and 84 then '65-84'
        else '85+'
    end as age_group,
    count(case when gender='Male' then 1 end) as male_count,
    count(case when gender='Female' then 1 end) as female_count
from customers
group by age_group
order by age_group;

select count(*) from customers as total_customer;

select 
    country,gender,COUNT(*) as total_customers
from customers
group by country, gender
order by country, gender;

select distinct(country) from customers;

select 
	c.name,
    c.gender,
    c.customer_key,  -- Include other relevant fields as needed
    s.order_date,
    c.birthday,
    TIMESTAMPDIFF(YEAR, c.birthday, s.order_date) -
    (date_format(s.order_date, '%m%d') < DATE_FORMAT(c.birthday, '%m%d')) as Age_When_Ordered
from 
    sales s
join 
    customers c on s.customer_key = c.customer_key;
    
-- 1) find the total number of customers in particular category and subcategory based on age group
select 
    p.category,p.subcategory,
    case 
        when c.age between 18 and 24 then '18-24'
        when c.age between 25 and 34 then '25-34'
        when c.age between 35 and 44 then '35-44'
        when c.age between 45 and 54 then '45-54'
        when c.age between 55 and 64 then '55-64'
        when c.age between 65 and 84 then '65-84'
        else '85+'
    end as age_group,
    COUNT(*) as interest_count
from sales s
join products p on s.product_key = p.product_key
join customers c on s.customer_key = c.customer_key
group by p.category, p.subcategory, age_group
order by p.category, p.subcategory, age_group;
    
    
-- 2) find the total sales by state
select 
    c.state,
    ROUND(SUM(s.quantity * (REPLACE(p.unit_price_usd, '$', '') + 0)), 2) AS total_sales
from sales s
join customers c on s.customer_key = c.customer_key
join products p on s.product_key = p.product_key
group by c.state
order by c.state asc;

-- 3) find the quantity bought by gender on category
select 
    c.gender,
    p.category,
    sum(s.quantity) as total_quantity
from sales s
join customers c on s.customer_key = c.customer_key
join products p on s.product_key = p.product_key
group by c.gender,p.category
order by c.gender,total_quantity DESC;

-- ------------------------------------------------------------ sales ----------------------------------------------------------------------------------------------------

-- 4) total sales values usd by store 
select 
    st.store_key,
    st.state,
    st.country,
    st.square_meters,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)) * e.exchange)) as total_sales_usd
from sales s
join store st on s.store_key = st.store_key
join products p on s.product_key = p.product_key
left join exchange_rates e on s.currency_code = e.currency
    and s.order_date = e.date
group by st.store_key, st.state, st.country, st.square_meters
order by store_key asc;

-- 5) top 10 sales values usd by store 
select 
    st.store_key,
    st.state,
    st.country,
    st.square_meters,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)) * e.exchange)) as total_sales_usd
from sales s
join store st on s.store_key = st.store_key
join products p on s.product_key = p.product_key
left join exchange_rates e on s.currency_code = e.currency
    and s.order_date = e.date
group by st.store_key, st.state, st.country, st.square_meters
order by total_sales_usd desc
limit 10;

-- 6) least 10 sales values usd by store 
select 
    st.store_key,
    st.state,
    st.country,
    st.square_meters,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)) * e.exchange)) as total_sales_usd
from sales s
join store st on s.store_key = st.store_key
join products p on s.product_key = p.product_key
left join exchange_rates e on s.currency_code = e.currency
    and s.order_date = e.date
group by st.store_key, st.state, st.country, st.square_meters
order by total_sales_usd asc
limit 10;

-- group store by country 
select 
    st.country,
    concat(lpad(min(st.store_key), 2, '0'), ' to ', lpad(max(st.store_key), 2, '0')) as store_range
from store st
group by st.country
order by st.country asc;

-- 7) find total_sales of each product
select 
    p.category,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales_usd
from sales s
join products p on s.product_key = p.product_key
group by p.category
order by total_sales_usd desc;

-- ------------------------------------------------------------ store ----------------------------------------------------------------------------------------------------
-- 8) total profit by currency code
select 
    s.currency_code,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales_usd
from sales s
join products p on s.product_key = p.product_key
group by currency_code;

-- find currency_code of couuntry 
select 
	st.country,
    s.currency_code,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales_usd
from sales s
join products p on s.product_key = p.product_key
join store st on st.store_key = s.store_key
group by st.country,s.currency_code
order by st.country, s.currency_code;   -- file name --> country_and_currency_code 

-- find how many stores opened in a year 
select
    year(open_date) as year_opened,
    count(store_key) as total_stores_opened
from store
group by year(open_date)
order by year_opened;  -- file name --> total_stores_opened_in_year 
 
-- 9) find profit and stores in state by store_age
select 
	s.state,
    s.store_age,
    sum(sales.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales
from 
    (select store_key, state, timestampdiff(year, open_date, curdate()) as store_age
     from store) s
join sales on s.store_key = sales.store_key
join products p on sales.product_key = p.product_key
group by s.state, s.store_age
order by s.store_age;    -- file name --> profit_by_store_age 

-- 10) top 10 store_key by sales
select
    s.store_key,
    st.country,
    st.state,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales
from sales s
join products p on s.product_key = p.product_key
join store st on s.store_key = st.store_key
group by s.store_key, st.country, st.state
order by total_sales desc
limit 10;

-- 11) least 10 store_key by sales
select
    s.store_key,
    st.country,
    st.state,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales
from sales s
join products p on s.product_key = p.product_key
join store st on s.store_key = st.store_key
group by s.store_key, st.country, st.state
order by total_sales asc
limit 10;

-- 12) profit by each month in a year of all stores 
select
    s.store_key,
    year(order_date) as year,
    date_format(order_date, '%b') AS month,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales
from sales s
join products p on s.product_key = p.product_key
join store st on s.store_key = st.store_key
group by s.store_key, year(order_date), date_format(order_date, '%b'),month(order_date)
order by s.store_key, year, month(order_date);     -- file name --> profit_by_stores_on_month 

-- 13) identify country with high customer demand
select 
    c.country,
    count(c.customer_key) as customer_count,
    sum(s.quantity) as total_sales_volume
from customers c
join sales s on c.customer_key = s.customer_key
group by c.country
order by total_sales_volume desc;    -- file name --> country_with_high_customer

-- identify country with fewer store
select 
    s.country,
    count(s.store_key) as store_count
from store s
group by s.country
order by store_count asc;  -- file name --> country_with_fewer_stores

-- combined data to identify underperforming country
select 
    a.country,
    a.customer_count,
    a.total_sales_volume,
    b.store_count,
    (a.total_sales_volume / b.store_count) as sales_per_store
from 
    (select 
         c.country,
         count(c.customer_key) as customer_count,
         sum(s.quantity) as total_sales_volume
     from customers c
     join sales s on c.customer_key = s.customer_key
     group by c.country) a
join 
    (select 
         s.country,
         count(s.store_key) as store_count
     from store s
     group by s.country) b
on a.country = b.country
order by sales_per_store desc;     -- underperforming_country 

-- ------------------------------------------------------------ Product ----------------------------------------------------------------------------------------------------

select distinct brand from products;   -- file name --> distinct_brand_names

select distinct category from products;  -- file name --> distinct_category_names

select distinct subcategory from products; -- file name --> distinct_subcategory_names

select sum((cast(replace(profit, '$', '') as decimal(18, 2)))) as Total_Profit from products;

select category, count(subcategory) as sub_category_count
from products
group by category;    -- file name --> subcategory_count

select category,sum((cast(replace(profit, '$', '') as decimal(18, 2)))) as Total_Profit from products
group by category;  -- file name --> profit_by_category

select subcategory,sum((cast(replace(profit, '$', '') as decimal(18, 2)))) as Total_Profit from products
group by subcategory;   -- file name --> profit_by_subcategory


-- 14) top selling products accross the region
select 
    p.product_name,
    p.category,
    p.subcategory,
    s.store_key,
    st.country,
    st.state,
    sum(s.quantity) as total_quantity_sold,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales
from sales s
join products p on s.product_key = p.product_key
join store st on s.store_key = st.store_key
group by p.product_name, p.category, p.subcategory, s.store_key, st.country, st.state
order by total_quantity_sold desc;

-- 15) total sales on monthly base for each category
select
	date_format(s.order_date, '%Y') AS year,
    date_format(s.order_date, '%M') as month,  
    p.category,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales 
from sales s
join products p on s.product_key = p.product_key
group by year, month, p.category
order by year asc;     -- file name --> total_sales_product_yearly

-- 16) total sales on yearly base for each category
select                       
    p.category,
    year(s.order_date) as year,   
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales 
from sales s
join products p on s.product_key = p.product_key
group by p.category, year(s.order_date)
order by p.category, year;    -- file name --> total_sales_product_yearly

-- 17) total_profit by brand
select 
    p.brand,
    sum(cast(replace(p.profit, '$', '') as decimal(18, 2))) as total_profit
from products p
group by p.brand
order by total_profit desc;  -- file name --> total_profit_by_brand

-- 18) total 10 product by sales volume
select 
    p.product_name,        
    sum(s.quantity) as total_sales_volume
from sales s
join products p on s.product_key = p.product_key
group by p.product_name
order by total_sales_volume desc
limit 10;                  -- file name --> top_10_by_sales_volume

-- 19) Products which are popular in different countries
select 
    st.country,
    p.product_name,
    sum(s.quantity) as total_quantity_sold
from sales s
join products p on s.product_key = p.product_key
join store st on s.store_key = st.store_key
join customers c on s.customer_key = c.customer_key
group by st.country, p.product_name
having sum(s.quantity) = (
    select max(total_quantity_sold)
    from (
        select 
            st.country,
            p.product_name,
            sum(s.quantity) as total_quantity_sold
        from sales s
        join products p on s.product_key = p.product_key
        join store st on s.store_key = st.store_key
        join customers c on s.customer_key = c.customer_key
        group by st.country, p.product_name
    ) as Subquery
    where Subquery.country = st.country)
order by total_quantity_sold desc;   -- file name --> popular_products_in_country

-- ------------------------------------------------------------ exchange_rates ----------------------------------------------------------------------------------------------------

-- 20) exchange rate fluctuate over time in different countries

select 
    c.country,
    date_format(er.Date, '%M') as month,
    date_format(er.Date, '%Y') as year,
    avg(er.exchange) as avg_exchange_rate
from sales s
join customers c on s.customer_key = c.customer_key
join exchange_rates er on s.currency_code = er.currency and s.order_date = er.Date
group by c.country, month, year
order by c.country, month;     -- file name --> er_fluctuate_diff_countries

-- 21) profitable currency type for the company
select 
    s.currency_code,
    sum(cast(replace(p.profit, '$', '') as decimal(18, 2)) * er.exchange) as total_profit_usd
from sales s
join products p on s.product_key = p.product_key
join exchange_rates er on s.currency_code = er.currency and s.order_date = er.Date
group by s.currency_code
order by total_profit_usd desc;  -- file name --> profitable_currency_type

-- 22) sales distribution by currency code
select 
    s.currency_code,
    sum(s.quantity * (cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2)))) as total_sales_usd
from sales s
join products p on s.product_key = p.product_key
group by s.currency_code
order by total_sales_usd desc;

select 
    p.product_key,
    p.product_name,
    s.currency_code,
    st.country,
    st.state,
    p.unit_cost_usd,
    p.unit_price_usd,
    er.exchange AS exchange_rate,
    ((cast(replace(p.unit_cost_usd, '$', '') as decimal(18, 2))) * er.exchange) as local_cost,
    ((cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2))) * er.exchange) as local_price,
    (((cast(replace(p.unit_price_usd, '$', '') as decimal(18, 2))) * er.exchange) - ((cast(replace(p.unit_cost_usd, '$', '') as decimal(18, 2))) * er.exchange)) as profit_margin
from sales s
join products p on s.product_key = p.product_key
join exchange_rates er on s.currency_code = er.currency and date(s.order_date) = date(er.Date)
join store st on s.store_key = st.store_key;  -- file name --> profit_margin



































