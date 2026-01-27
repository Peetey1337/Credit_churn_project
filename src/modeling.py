import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTENC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    roc_curve,
)
import matplotlib.pyplot as plt
from __init__ import get_logger
from config import RANDOM_STATE, TEST_SIZE, TARGET_COL, PLOTS_DIR

logger = get_logger(__name__)


def train_test_scale(df_encoded, num_cols):
    X = df_encoded.drop(columns=[TARGET_COL])
    y = df_encoded[TARGET_COL]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    scaler = StandardScaler()
    X_train_s = X_train.copy()
    X_test_s = X_test.copy()
    X_train_s[num_cols] = scaler.fit_transform(X_train[num_cols])
    X_test_s[num_cols] = scaler.transform(X_test[num_cols])
    return X_train, X_test, X_train_s, X_test_s, y_train, y_test, scaler


def fit_logreg(X_train_s, y_train):
    logger.info("Training Logistic Regression (balanced)")
    model = LogisticRegression(
        class_weight="balanced", max_iter=1000, random_state=RANDOM_STATE
    )
    model.fit(X_train_s, y_train)
    return model


def fit_logreg_smotenc(X_train_s, y_train):
    logger.info("Training Logistic Regression with SMOTENC (balanced)")
    cat_features_to_smote = ["Income_Category_OE", "Education_Level_OE"]
    categorical_indices = [
        X_train_s.columns.get_loc(col) for col in cat_features_to_smote
    ]
    smote = SMOTENC(categorical_features=categorical_indices, random_state=RANDOM_STATE)
    X_resampled, y_resampled = smote.fit_resample(X_train_s, y_train)
    model = LogisticRegression(
        class_weight="balanced", max_iter=1000, random_state=RANDOM_STATE
    )
    model.fit(X_resampled, y_resampled)
    return model


def fit_rf(X_train, y_train):
    logger.info("Training Random Forest (class_weight=balanced)")
    model = RandomForestClassifier(class_weight="balanced", random_state=RANDOM_STATE)
    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test, name: str):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_proba),
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
    }
    for metric in metrics:
        logger.info(f"{name} metrics: {metric} = {metrics[metric]}")
    plot_roc(y_test, y_proba, name)
    return metrics


def plot_roc(y_test, y_proba, name: str):
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(fpr, tpr, label=f"{name} ROC (AUC={roc_auc_score(y_test, y_proba):.2f})")
    ax.plot([0, 1], [0, 1], "k--")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title(f"ROC Curve - {name}")
    ax.legend(loc="lower right")
    fig.tight_layout()
    out = PLOTS_DIR / f"roc_{name.lower().replace(' ', '_')}.png"
    fig.savefig(out)
    logger.info(f"Saved {name} ROC plot:")
    plt.close(fig)
