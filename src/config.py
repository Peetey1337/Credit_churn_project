import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "BankChurners.csv"
PLOTS_DIR = PROJECT_ROOT / "plots"
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

# Feature groups (from notebook)
TARGET_COL = "Attrition_Flag"

EDUCATION_ORDER = [
    "Unknown",
    "Uneducated",
    "High School",
    "College",
    "Graduate",
    "Post-Graduate",
    "Doctorate",
]
INCOME_ORDER = [
    "Unknown",
    "Less than $40K",
    "$40K - $60K",
    "$60K - $80K",
    "$80K - $120K",
    "$120K +",
]
CARD_ORDER = ["Blue", "Silver", "Gold", "Platinum"]
RANDOM_STATE = 109220
TEST_SIZE = 0.2
