WITH unique_customer AS (
    select customer_id, 
    count(distinct visitor_id) AS count_visitors
     from  {{ ref('stg_tracking') }}  
where customer_id is not null
group by 1 
order by 2 desc 
)

SELECT*
FROM unique_customer


