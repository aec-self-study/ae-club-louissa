{%- set categories = ['coffee beans', 'merch', 'brewing supplies'] -%}

select
  date_trunc(sold_at, month) as date_month,
  {%- for category in categories %}
  sum(case when product_category = '{{ category }}' then price end) as {{ category|replace(' ', '_') }}_sales
  {%- if not loop.last %}, {% endif %}
  {%- endfor %}
from {{ ref('stg_sample_data') }}
group by 1