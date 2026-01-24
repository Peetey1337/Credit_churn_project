# Credit Churn Data Science Report

## Project Overview
This report documents basic notebook data science workflow for predicting customer churn in a banking dataset, as performed in the analysis.ipynb notebook. The goal is to identify customers likely to leave the bank (churn) using interpretable and robust machine learning models.

---

## 1. Data Loading & Initial Exploration
- **Source:** BankChurners.csv, [Kaggle.com](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers)
- **Steps:**
  - Loaded data using pandas.
  - Dropped irrelevant columns.
  - Checked for missing values and duplicates (none significant).
  - Inspected feature types and distributions.

---

## 2. Feature Engineering & Preprocessing
- **Feature Types:**
  - Numerical, Categorical, Ordinal features identified.
  - Ordinal features: Education_Level, Income_Category and few numerical discrete features
- **Handling Unknowns:**
  - "Unknown" treated as informative, not missing.
- **Outlier Analysis:**
  - Outliers present but not removed (important for banking data).

---

## 3. Statistical Analysis
- **Tests Used:**
  - Mann-Whitney U for numerical features.
  - Chi-Squared for categorical features.
  - Spearman correlation for ordinal features.
- **Outcome:**
  - Identified features significantly associated with churn.

---

## 4. Encoding
- **One-Hot Encoding (OHE):**
  - Gender, Card_Category, Marital_Status (nominal features).
- **Ordinal Encoding (OE):**
  - Education_Level, Income_Category (ordinal features with the Unknown value kept).
- **Target Variable:**
  - Attrition_Flag mapped to binary (0: Existing, 1: Attrited).

---

## 5. Train-Test Split & Scaling
- **Split:**
  - 80/20 stratified split to prevent data leakage.
- **Scaling:**
  - StandardScaler applied to numerical features (for logistic regression only).

---

## 6. Modeling & Evaluation
### Logistic Regression (with class_weight='balanced')
- **Metrics:**
  - Accuracy, Precision, Recall, F1, ROC AUC, Confusion Matrix, Classification Report.
- **Results:**
  - Recall: 0.862 (best for catching churners)
  - F1 Score: 0.653
  - High ROC AUC (0.928)
- **Interpretation:**
  - See the #8 point of the report below.

### Logistic Regression with SMOTE
- **SMOTE:**
  - Synthetic Minority Over-sampling Technique used to balance training data.
- **Metrics:**
  - Similar evaluation as above however worse Recall and F1-score values.
- **Results:**
  - Recall: 0.809
  - F1 Score: 0.667 
  - HIGH ROC AUC (0.919)

- **Interpretation:**
  - Irrelevant differences between first Logistic Regression

### Random Forest Classifier
- **Metrics:**
  - Recall: 0.742
  - F1 Score: 0.827
  - HIGH ROC AUC (0.991)
- **Interpretation:**
  - Higher precision and ROC AUC, but lower recall than logistic regression.

---

## 7. Model Comparison & Business Implications
- **Logistic Regression:**
  - Higher recall, better for catching most churners (minimizing missed churn).
- **Random Forest:**
  - Higher precision and ROC AUC, better for confident predictions (minimizing false alarms).
- **SMOTE:**
  - Balances class distribution, improves minority class detection however the scores were very simmilar to the Logistic Regression model with balanced class parameter.
- **ROC Curves:**
  - Plotted for all models, showing discrimination ability.

---

## 8. Interpretation from the Logistic Regression
**Most interesting and valuable insights from the dataset**
  - For each unit increase in Total_Trans_Amt, the odds of churn increase by a factor of 6.48. This is a strong positive effect telling us that higher transaction amounts are strongly associated with increased churn risk.
  - Each additional contact in the last 12 months increases the odds of churn by 76%. More frequent contact is associated with higher churn risk, possibly indicating dissatisfaction or issues with the approach to the customer.
  - A higher level of income increase the odds of churn by 21% per level. Higher income is slightly associated with higher churn risk.

### Negative Effects
  - Each additional transaction count significantly decreases the odds of churn by ~95%. More transactions are strongly protective against churn.
  - What is more, being male reduces the odds of churn by 61% compared to the reference group (female). Males are less likely to churn in our bank.

## 9. Recommendations for the model
- Choose model based on business priorities:
  - If missing churners is costly, prefer Logistic Regression.
  - If false positives are costly, prefer Random Forest.
- As always consider interpretability (Logistic Regression) vs. predictive power (Random Forest).

---

## 10. Recommendations for the business
- The bank should focus on high-value, high-contact, and higher-income customers with proactive, personalized engagement. Offer them exclusive programs, wealth management services or invite them to special events to make customers feel valued.
- Investigate the potential customer service malfunctioning. Analyze deeply the source of higher churn. Implement surveys after contacts and improve response times.
- Consider targeted engagement strategies for female customers such as special products, events or extra support.

---

## 11. Potential extentions of the project 
- Feature importance analysis for a Random Forest.
- Hyperparameter tuning.
- Extended Feature Engineering

---

*This report summarizes the full workflow, results, and business implications of the churn prediction analysis. For code and details, see analysis.ipynb.*
