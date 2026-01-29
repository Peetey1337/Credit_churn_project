# Credit Churn Project – Python & SQL

## Overview

This project provides a full pipeline for credit churn analysis using both Python and MySQL.  
It includes automated EDA, preprocessing, visualization, modeling, and an alternative SQL-based analysis. The goal of this project is to compare three different models and choose the best one that fits the user's needs. There is another README file in the notebooks folder that dives deeper into the specifics and there's also more business interpretation (features impact on the churn, importance of features in modeling etc.)

## Features

- Data loading from CSV or MySQL
- Automated EDA, preprocessing, and feature engineering (Python)
- Model training and evaluation (Two types of Logistic Regression and Random Forest)
- All plots saved to `/plots`
- Logging of all pipeline steps
- Export of processed data to MySQL (if database is made and commented out)
- Alternative SQL scripts for EDA and business queries

## Dataset

- Bank Churners dataset (Kaggle) https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers


## How to Run

1. **Install MySQL Server** (optional, for SQL features)
2. **Create virtual environment**
3. **Install requirements:**  
   `pip install -r requirements.txt`
4. **Configure environment:**  
   Copy `.env.example` to `.env` and fill in your DB credentials
5. **Run the automated pipeline:**  
   `python -m src.pipeline`
6. **(Optional) Run SQL analysis:**  
   Use queries in `/SQL` for database-side EDA and ENCODING

## Structure

- `/src` – Modular Python pipeline (data loading, preprocessing, modeling, etc.)
- `/notebooks` – Jupyter notebook for full exploration
- `/SQL` – Example SQL queries for EDA and business analysis
- `/plots` – All generated plots
- `/data` – Raw data files

## Notes

- All logs are saved in `/logs`
- The pipeline can export processed data to MySQL if DB connection is available (remember to first create a database in MySQL and change the name in the .env file)
- You can use either the Python pipeline or SQL scripts for EDA, business analysis or Encoding
---