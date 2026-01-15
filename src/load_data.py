import pandas as pd
from sqlalchemy import create_engine
from config import DB_CONFIG

engine = create_engine(
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

df = pd.read_csv("data/raw/creditcard.csv")

df.to_sql(
    "creditcard_transactions",
    engine,
    if_exists="replace",
    index=False,
    chunksize=5000
)
