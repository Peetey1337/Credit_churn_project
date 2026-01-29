import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from __init__ import get_logger

logger = get_logger(__name__)
load_dotenv()


def load_csv(path):
    logger.info(f"Loading CSV from {path}")
    return pd.read_csv(path)


def make_engine():
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME")
    url = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    return create_engine(url)


def to_mysql(df, table_name: str):
    engine = make_engine()
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info(f"Writing DataFrame to MySQL table '{table_name}'")
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    except SQLAlchemyError as e:
        logger.warning(f"Skipping MySQL export: connection failed ({e})")
