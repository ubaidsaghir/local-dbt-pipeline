{{ config(materialized='table') }}

select
    order_id,
    customer_id,
    customer_name,
    product_category,
    quantity,
    unit_price,
    quantity * unit_price as total_amount,
    order_date,
    status
from {{ ref('orders') }}
where status = 'Completed'