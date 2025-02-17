{{ config(materialized='table') }}

with source as (
   select* from {{ source('source_coffee_shop', 'customers')}}
),

renamed as(

   select *
      from source
) 

select* from renamed
