{{config(materialized='table')}}

with order_items as (
  select*
  from `analytics-engineers-club.coffee_shop.order_items` 
),

renamed as(

   select *
   from order_items

) 

select* from renamed
