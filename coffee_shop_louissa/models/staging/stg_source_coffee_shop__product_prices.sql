
with source as (

    select * from {{ source('coffee_shop', 'src_product_prices') }}

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

