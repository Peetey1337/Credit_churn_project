"""
End-to-end pipeline orchestrating EDA, preprocessing, visualization, and modeling.
"""

import pandas as pd
from config import DATA_PATH
from __init__ import get_logger
from load_data import load_csv, to_mysql
from preprocessing import (
    initial_clean,
    set_categoricals,
    encode,
    get_numerical_cols,
    get_categorical_cols,
)
from eda import (
    missing_values,
    duplicates_count,
    histograms,
    boxplots,
    countplots,
    correlation_heatmap,
)
from modeling import train_test_scale, fit_logreg, fit_logreg_smotenc, fit_rf, evaluate

logger = get_logger(__name__)


def run_pipeline():
    # Load
    df = load_csv(DATA_PATH)

    # EDA basics
    miss_df = missing_values(df)
    dup_count = duplicates_count(df)
    logger.info(f"Missing values:\n{miss_df}")
    logger.info(f"Duplicate rows: {dup_count}")

    # Preprocess
    df = initial_clean(df)
    # Optional: export unprocessed data to DB (if no database is used, comment out)
    # to_mysql(df, table_name="bank_churners_unprocessed")
    df = set_categoricals(df)
    num_cols = get_numerical_cols(df)
    cat_cols = get_categorical_cols(df)

    # Visuals (saved to plots/)
    histograms(df, num_cols)
    boxplots(df, num_cols)
    countplots(df, cat_cols)
    correlation_heatmap(df, num_cols)
    logger.info("EDA visualizations saved in plots/.")

    # Encode
    df_encoded = encode(df)
    num_cols = get_numerical_cols(df_encoded)
    cat_cols = get_categorical_cols(df_encoded)

    # Split/scale
    X_train, X_test, X_train_s, X_test_s, y_train, y_test, _ = train_test_scale(
        df_encoded, num_cols
    )

    # Models
    logreg = fit_logreg(X_train_s, y_train)
    logreg_smotenc = fit_logreg_smotenc(X_train_s, y_train)
    rf = fit_rf(X_train, y_train)

    metrics_logreg = evaluate(logreg, X_test_s, y_test, "Logistic Regression")
    metrics_logreg_smotenc = evaluate(
        logreg_smotenc, X_test_s, y_test, "Logistic Regression SMOTE"
    )
    metrics_rf = evaluate(rf, X_test, y_test, "Random Forest")
    metrics_df = pd.DataFrame(
        [
            {"Model": "Logistic Regression", **metrics_logreg},
            {"Model": "Logistic Regression SMOTE", **metrics_logreg_smotenc},
            {"Model": "Random Forest", **metrics_rf},
        ]
    )

    logger.info("\nModel Comparison:\n%s", metrics_df.to_string(index=False))

    # Optional: export to DB (if no database is used, comment out)
    # to_mysql(df_encoded, table_name="bank_churners_processed")


if __name__ == "__main__":
    run_pipeline()
