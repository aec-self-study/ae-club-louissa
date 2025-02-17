{{config(materialized='table')}}

with order as (
  select*
  from `analytics-engineers-club.coffee_shop.order` 
),

renamed as(

   select *
   from order

) 

select* from renamed