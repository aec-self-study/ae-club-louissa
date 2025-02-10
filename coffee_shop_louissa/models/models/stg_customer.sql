{{ config(materialized='table') }}

with source as (
   select* from {{ source('source_raw', 'customers')}}
),

renamed as(

   select 
   customer_id
   from source
) 

select* from renamed
