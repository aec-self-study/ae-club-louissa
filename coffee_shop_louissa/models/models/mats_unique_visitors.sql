{{ config(materialized='table') }}


WITH unique AS (
    SELECT 
        COALESCE(customer_id, visitor_id) AS unique_visitor,  
        device_type,
        id,
        timestamp,
        page
     from  {{ ref('stg_tracking') }}  
),

sessions AS (
    SELECT 
        *,
        -- Zeitdifferenz in Minuten zur vorherigen Zeile berechnen
        TIMESTAMP_DIFF(timestamp, 
            LAG(timestamp) OVER (PARTITION BY unique_visitor ORDER BY timestamp), 
            MINUTE) AS time_diff,

        -- Neue Session starten, wenn der Zeitunterschied > 30 Minuten ist
        CASE 
            WHEN TIMESTAMP_DIFF(timestamp, 
                LAG(timestamp) OVER (PARTITION BY unique_visitor ORDER BY timestamp), 
                MINUTE) > 30 
            OR LAG(timestamp) OVER (PARTITION BY unique_visitor ORDER BY timestamp) IS NULL 
            THEN 1 
            ELSE 0 
        END AS new_session_flag
    FROM unique
),

session_numbering AS (
    SELECT 
        *,
        -- Session-Nummer hochzählen
        SUM(new_session_flag) OVER (PARTITION BY unique_visitor ORDER BY timestamp) AS session_number
    FROM sessions
)

SELECT 
    unique_visitor,
    timestamp,
    session_number,
    -- Kombinierte Session-ID aus unique_visitor und session_number
    CONCAT(unique_visitor, '_', session_number) AS session_id,
    device_type,
    page
FROM session_numbering
