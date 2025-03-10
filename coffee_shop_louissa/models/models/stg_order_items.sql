{{ config(materialized='table') }}

with source as (
   select* from {{ source('coffee_shop', 'src_order_items')}}
),

renamed as(

   select *
      from source
) 

select* from renamed
