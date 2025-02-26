with customer_acquisition as (
    -- Holen der frühesten Bestellung je Kunde (als "Akquisitionsdatum")
    select
        customer_id,
        min(sold_at) as first_purchase_date
    from {{ ref('stg_sample_data') }} 
    group by customer_id
),


weekly_revenue as (
    -- Berechnung des Umsatzes je Kunde pro Woche
    select
        customer_id,
        date_trunc(sold_at, week) as week_start_date,
        sum(price) as revenue
    from {{ ref('stg_sample_data') }} -- Referenz zur stg_sample_data-Tabelle
    group by customer_id, date_trunc(sold_at, week)
),

weeks as (
    -- Erzeugen der wöchentlichen Zeitreihen für jeden Kunden basierend auf dem Akquisitionsdatum
    select
        customer_id,
        first_purchase_date
    from customer_acquisition
),

generated_weeks as (
    -- Generieren von Wochen basierend auf der Differenz zwischen dem ersten Kaufdatum und dem aktuellen Datum
    select
        w.customer_id,
        date_add(cast(w.first_purchase_date as date), interval week_num week) as week_start_date
    from weeks w
    cross join unnest(generate_array(0, date_diff(current_date(), cast(w.first_purchase_date as date), week))) as week_num
),

joined_data as (
    -- Verknüpfung der generierten Wochen mit den berechneten Umsatzdaten und Auffüllen der Lücken mit 0
    select
        g.customer_id,
        g.week_start_date,
        coalesce(r.revenue, 0) as revenue
    from generated_weeks g
    left join weekly_revenue r
        on g.customer_id = r.customer_id
        and g.week_start_date = cast(r.week_start_date as date)

),

cumulative_data as (
    -- Berechnung des kumulierten Umsatzes und Zuweisung einer Wochenzahl
    select
        customer_id,
        week_start_date,
        revenue,
        sum(revenue) over (partition by customer_id order by week_start_date) as cumulative_revenue,
        row_number() over (partition by customer_id order by week_start_date) as week
    from joined_data
)

select
    customer_id,
    week,
    revenue,
    cumulative_revenue
From cumulative_data