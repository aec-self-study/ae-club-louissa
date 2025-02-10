{{ config(materialized='table') }}

with source as (
   select* from {{ source('source_raw', 'customers')}}
),

renamed as(

   select *
      from source
) 

select* from renamed
