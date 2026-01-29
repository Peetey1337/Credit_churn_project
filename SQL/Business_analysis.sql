select * from bank_churners_unprocessed;

ALTER TABLE bank_churners_unprocessed
ADD COLUMN CLIENTNUM INT NOT NULL auto_increment primary key first;

#attritions by age
SELECT
    attrition_flag,
    COUNT(*)            AS customers,
    AVG(customer_age)   AS avg_age,
    MIN(customer_age)   AS min_age,
    MAX(customer_age)   AS max_age
FROM bank_churners_unprocessed
GROUP BY attrition_flag;


#attritions by income_category
SELECT 
    income_category,
    ROUND(SUM(attrition_flag = 'Attrited Customer') / COUNT(*) * 100,
            2) AS churn_rate
FROM
    bank_churners_unprocessed
GROUP BY income_category
ORDER BY churn_rate DESC;

#attritions by number of bank products

SELECT
    total_relationship_count,
    COUNT(*) AS customers,
    SUM(attrition_flag = 'Attrited Customer') AS churned,
    AVG(Attrition_Flag = 'Attrited Customer') as churn_rate
FROM bank_churners_unprocessed
GROUP BY total_relationship_count
ORDER BY total_relationship_count;

SELECT
  Marital_Status,
  COUNT(*) AS n,
  AVG(Attrition_Flag = 'Attrited Customer') AS churn_rate
FROM bank_churners_unprocessed
GROUP BY Marital_Status
order by churn_rate desc;

SELECT
  Education_Level,
  COUNT(*) AS n,
  AVG(Attrition_Flag = 'Attrited Customer') AS churn_rate
FROM bank_churners_unprocessed
GROUP BY Education_Level
order by churn_rate desc;
