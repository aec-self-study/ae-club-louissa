
with source as (

    select * from {{ source('source_coffee_shop', 'product_prices') }}

),

renamed as (

    select
        id,
        product_id,
        price,
        created_at,
        ended_at

    from source

)

select * from renamed

