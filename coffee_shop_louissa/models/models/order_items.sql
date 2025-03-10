{{config(materialized='table')}}

with order_items as (
  select*
  from {{ref('stg_order_items')}}
),

renamed as(

   select *
   from order_items

) 

select* from renamed
