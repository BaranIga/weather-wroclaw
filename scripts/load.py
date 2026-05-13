import os
from config import DATA_PATH

def save_to_csv(df):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    df.to_csv(DATA_PATH, index=False)