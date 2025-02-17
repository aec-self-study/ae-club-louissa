WITH weekly_revenue AS (
    SELECT
        FORMAT_TIMESTAMP('%Y-%m-%d', TIMESTAMP_TRUNC(sold_at, WEEK)) AS week,
        product_category,
        SUM(price) AS revenue
    FROM {{ ref('stg_sample_data') }} 
    GROUP BY 1, 2
)

SELECT
    week,
    product_category,
    revenue
FROM weekly_revenue
ORDER BY week, product_category
