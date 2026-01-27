import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from __init__ import get_logger
from config import PLOTS_DIR, TARGET_COL

logger = get_logger(__name__)
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)


def save_plot(fig, name: str):
    path = PLOTS_DIR / name
    fig.tight_layout()
    fig.savefig(path)


def missing_values(df: pd.DataFrame):
    mc = df.isnull().sum()
    pct = (mc / len(df) * 100).round(2)
    return pd.DataFrame({"Missing_Count": mc, "Percentage": pct})


def duplicates_count(df: pd.DataFrame) -> int:
    return int(df.duplicated().sum())


def histograms(df: pd.DataFrame, numeric_cols):
    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(df[col], kde=True, color="blue", bins=30, ax=ax)
        ax.set_title(f"Histogram of {col}")
        save_plot(fig, f"hist_{col}.png")
        plt.close(fig)


def boxplots(df: pd.DataFrame, numeric_cols):
    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.boxplot(
            x=df[col],
            ax=ax,
            medianprops={"color": "red"},
            boxprops={"facecolor": "lightblue"},
        )
        ax.set_title(f"Box Plot of {col}")
        save_plot(fig, f"box_{col}.png")
        plt.close(fig)


def countplots(df: pd.DataFrame, categorical_cols):
    for col in categorical_cols:
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.countplot(data=df, x=col, hue=TARGET_COL, ax=ax)
        ax.set_title(f"Count Plot of {col}")
        save_plot(fig, f"count_{col}.png")
        plt.close(fig)


def correlation_heatmap(df: pd.DataFrame, numeric_cols):
    corr = df[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        square=True,
        cbar_kws={"shrink": 0.8},
        ax=ax,
    )
    ax.set_title("Correlation Matrix of Numerical Features")
    save_plot(fig, "corr_matrix.png")
    plt.close(fig)
