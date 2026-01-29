-- CREATE AND USE DATABASE
CREATE DATABASE bank_churn;
USE bank_churn;

select * from bank_churners_unprocessed;

-- ADD CLIENT NUM COLUMN IF IT DOESNT EXISTS
ALTER TABLE bank_churners_unprocessed
ADD COLUMN CLIENTNUM INT NOT NULL auto_increment primary key first;

-- 2. Map ordinal features to integers (Education_Level, Income_Category, Card_Category)
ALTER TABLE bank_churners_unprocessed
    ADD COLUMN Education_Level_OE INT,
    ADD COLUMN Income_Category_OE INT,
    ADD COLUMN Card_Category_OE INT;
    
    
UPDATE bank_churners_unprocessed
SET Education_Level_OE = CASE Education_Level
    WHEN 'Unknown' THEN 0
    WHEN 'Uneducated' THEN 1
    WHEN 'High School' THEN 2
    WHEN 'College' THEN 3
    WHEN 'Graduate' THEN 4
    WHEN 'Post-Graduate' THEN 5
    WHEN 'Doctorate' THEN 6
    ELSE NULL END
WHERE CLIENTNUM > 0;

UPDATE bank_churners_unprocessed
SET Income_Category_OE = CASE Income_Category
    WHEN 'Unknown' THEN 0
    WHEN 'Less than $40K' THEN 1
    WHEN '$40K - $60K' THEN 2
    WHEN '$60K - $80K' THEN 3
    WHEN '$80K - $120K' THEN 4
    WHEN '$120K +' THEN 5
    ELSE NULL END
WHERE CLIENTNUM > 0;


-- 3. One-hot encode Gender (Male=1, Female=0)
ALTER TABLE bank_churners_unprocessed ADD COLUMN Gender_Male INT;
UPDATE bank_churners_unprocessed SET Gender_Male = CASE WHEN Gender = 'M' THEN 1 ELSE 0 END
WHERE CLIENTNUM > 0;

-- 4. One-hot encode Card_Category (except Platinum as reference)
ALTER TABLE bank_churners_unprocessed
    ADD COLUMN Card_Category_Blue INT DEFAULT 0,
    ADD COLUMN Card_Category_Silver INT DEFAULT 0,
    ADD COLUMN Card_Category_Gold INT DEFAULT 0;

UPDATE bank_churners_unprocessed SET Card_Category_Blue = CASE WHEN Card_Category = 'Blue' THEN 1 ELSE 0 END WHERE CLIENTNUM > 0;
UPDATE bank_churners_unprocessed SET Card_Category_Silver = CASE WHEN Card_Category = 'Silver' THEN 1 ELSE 0 END WHERE CLIENTNUM > 0;
UPDATE bank_churners_unprocessed SET Card_Category_Gold = CASE WHEN Card_Category = 'Gold' THEN 1 ELSE 0 END WHERE CLIENTNUM > 0;

-- 5. One-hot encode Marital_Status (except Married as reference)
ALTER TABLE bank_churners_unprocessed
    ADD COLUMN Marital_Status_Single INT DEFAULT 0,
    ADD COLUMN Marital_Status_Divorced INT DEFAULT 0,
    ADD COLUMN Marital_Status_Unknown INT DEFAULT 0;

UPDATE bank_churners_unprocessed SET Marital_Status_Single = CASE WHEN Marital_Status = 'Single' THEN 1 ELSE 0 END WHERE CLIENTNUM > 0;
UPDATE bank_churners_unprocessed SET Marital_Status_Divorced = CASE WHEN Marital_Status = 'Divorced' THEN 1 ELSE 0 END WHERE CLIENTNUM > 0;
UPDATE bank_churners_unprocessed SET Marital_Status_Unknown = CASE WHEN Marital_Status = 'Unknown' THEN 1 ELSE 0 END WHERE CLIENTNUM > 0;

-- 6. Map Attrition_Flag to binary
UPDATE bank_churners_unprocessed SET Attrition_Flag = CASE WHEN Attrition_Flag = 'Attrited Customer' THEN 1 ELSE 0 END 
WHERE CLIENTNUM > 0;
-- modify the type of feature to int
ALTER TABLE bank_churners_unprocessed
MODIFY column Attrition_Flag INT;


-- 7. Drop original encoded columns if desired
ALTER TABLE bank_churners_unprocessed
    DROP COLUMN CLIENTNUM,
    DROP COLUMN Gender,
    DROP COLUMN Card_Category,
    DROP COLUMN Marital_Status,
    DROP COLUMN Education_Level,
    DROP COLUMN Income_Category;
    





