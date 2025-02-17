{{ config(materialized='table') }}

with source as (
   select* from {{ source('source_sample_data', 'order_items')}}
),

renamed as(

   select *
      from source
) 

select* from renamed
