-- Quick cleaning process in SQL

-- Query to find duplicates based on specific columns (e.g., CLIENTNUM and Attrition_Flag)
SELECT CLIENTNUM, Attrition_Flag, COUNT(*) as duplicate_count
FROM bank_churners_unprocessed
GROUP BY CLIENTNUM, Attrition_Flag
HAVING COUNT(*) > 1;

-- Query to count the number of nulls for each column in the bank_churners table (can add more)
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN Education_Level IS NULL THEN 1 ELSE 0 END) AS missing_education_level,
    SUM(CASE WHEN Income_Category IS NULL THEN 1 ELSE 0 END) AS missing_income_category,
    SUM(CASE WHEN Card_Category IS NULL THEN 1 ELSE 0 END) AS missing_card_category,
    SUM(CASE WHEN Total_Relationship_Count IS NULL THEN 1 ELSE 0 END) AS missing_total_relationship_count,
    SUM(CASE WHEN Months_Inactive_12_mon IS NULL THEN 1 ELSE 0 END) AS missing_months_inactive,
    SUM(CASE WHEN Contacts_Count_12_mon IS NULL THEN 1 ELSE 0 END) AS missing_contacts_count,
    SUM(CASE WHEN Attrition_Flag IS NULL THEN 1 ELSE 0 END) AS missing_attrition_flag
FROM bank_churners_unprocessed;


-- Missing values in the dataset
select count(*) as total_rows, sum(CASE WHEN Attrition_Flag IS NULL THEN 1 ELSE 0 END) as missing_values
from bank_churners_unprocessed;


