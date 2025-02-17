{{config(materialized='table')}}

with tracking as (
  select*
  from `analytics-engineers-club.web_tracking.pageviews` 
),

renamed as(

   select *
   from tracking

) 

select* from renamed