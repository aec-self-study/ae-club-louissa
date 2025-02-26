{{config(materialized='table')}}

SELECT * 
  from {{ref('mats_customers_cluster')}}
WHERE customer_id = 'f6456ecd-582f-47a3-a405-ab9dbc816df9'