SELECT * FROM `aec-students.dbt_louissa.mats_customers` 
WHERE NOT REGEXP_CONTAINS(email, r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}")