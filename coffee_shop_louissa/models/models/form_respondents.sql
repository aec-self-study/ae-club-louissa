{{ config(
    materialized='table'
 ) }}
 
with events as (
    select * from {{source('coffee_shop', 'src_form_events') }}
 ),
 
aggregated as (
    select
       github_username,
               min(timestamp) as first_form_entry,
     max(timestamp) as last_form_entry,
     count(*) as number_of_entries
    from events
  group by 1
 )
 
select * from aggregated