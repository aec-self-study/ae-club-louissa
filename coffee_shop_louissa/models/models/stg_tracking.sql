{{ config(materialized='table') }}

with source as (
   select* from {{ source('source_web_tracking', 'pageviews')}}
),

renamed as(

   select *
      from source
) 

select* from renamed
