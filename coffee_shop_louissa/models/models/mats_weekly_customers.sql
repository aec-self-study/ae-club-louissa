WITH first_order AS (
    SELECT
        customer_id,
        MIN(TIMESTAMP_TRUNC(sold_at, WEEK)) AS first_order_week
    FROM {{ ref('stg_sample_data') }}  
    GROUP BY customer_id
),

weekly_revenue AS (
    SELECT
        FORMAT_TIMESTAMP('%Y-%m-%d', TIMESTAMP_TRUNC(sold_at, WEEK)) AS week,
        customer_id,
        SUM(price) AS revenue
    FROM {{ ref('stg_sample_data') }}  
    GROUP BY 1, 2
),

customer_type AS (
    SELECT
        w.week,
        w.customer_id,
        CASE
            WHEN TIMESTAMP(w.week) = f.first_order_week THEN 'new'
            ELSE 'returning'
        END AS customer_status,
        w.revenue
    FROM weekly_revenue w
    JOIN first_order f ON w.customer_id = f.customer_id
)

SELECT
    week,
    customer_status,
    SUM(revenue) AS total_revenue
FROM customer_type
GROUP BY 1, 2
ORDER BY week, customer_status
