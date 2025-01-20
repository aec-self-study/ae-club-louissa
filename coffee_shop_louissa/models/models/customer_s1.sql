{{config(materialized='table')}}

  select
     customer_id

  from `analytics-engineers-club.coffee_shop.orders` 
