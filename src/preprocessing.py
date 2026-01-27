import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from __init__ import get_logger
from config import (
    TARGET_COL,
    EDUCATION_ORDER,
    INCOME_ORDER,
    CARD_ORDER,
)

logger = get_logger(__name__)


def initial_clean(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Dropping last two columns and CLIENTNUM (if present)")
    df = df.copy()
    df = df.iloc[:, :-2]
    df = df.drop(columns=["CLIENTNUM"], errors="ignore")
    return df


def set_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Setting categorical orders")
    df = df.copy()
    df["Education_Level"] = pd.Categorical(
        df["Education_Level"], categories=EDUCATION_ORDER, ordered=True
    )
    df["Income_Category"] = pd.Categorical(
        df["Income_Category"], categories=INCOME_ORDER, ordered=True
    )
    df["Card_Category"] = pd.Categorical(
        df["Card_Category"], categories=CARD_ORDER, ordered=True
    )
    return df


def encode(df: pd.DataFrame):
    logger.info("Encoding categorical and ordinal features")
    df = df.copy()
    ordinal_cols = ["Education_Level", "Income_Category"]
    oe = OrdinalEncoder(categories=[EDUCATION_ORDER, INCOME_ORDER])
    df[[c + "_OE" for c in ordinal_cols]] = oe.fit_transform(df[ordinal_cols]).astype(
        int
    )

    df = pd.get_dummies(df, columns=["Gender"], drop_first=True, dtype=int)
    df = pd.concat(
        [
            df,
            pd.get_dummies(df["Card_Category"], prefix="Card_Category", dtype=int).drop(
                columns=["Card_Category_Platinum"], errors="ignore"
            ),
        ],
        axis=1,
    )
    df = pd.concat(
        [
            df,
            pd.get_dummies(
                df["Marital_Status"], prefix="Marital_Status", dtype=int
            ).drop(columns=["Marital_Status_Married"], errors="ignore"),
        ],
        axis=1,
    )

    df["Attrition_Flag"] = df["Attrition_Flag"].map(
        {"Existing Customer": 0, "Attrited Customer": 1}
    )

    df = df.drop(columns=ordinal_cols + ["Card_Category", "Marital_Status"])
    return df


def get_numerical_cols(df_encoded: pd.DataFrame):
    num_cols = df_encoded.select_dtypes(
        include=["int64", "float64", "int32", "float32"]
    ).columns.tolist()
    if TARGET_COL in num_cols:
        num_cols.remove(TARGET_COL)
    return num_cols


def get_categorical_cols(df_encoded: pd.DataFrame):
    cat_cols = df_encoded.select_dtypes(
        include=["category", "object", "str"]
    ).columns.tolist()
    if TARGET_COL in cat_cols:
        cat_cols.remove(TARGET_COL)
    return cat_cols
