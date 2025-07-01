# Data preprocessing logic
import pandas as pd
import os
from sklearn.datasets import load_iris

# Simulate raw data saving
def save_raw_data():
    iris = load_iris(as_frame=True)
    df = iris.frame
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/iris.csv", index=False)

# Load raw, clean, and save processed
def preprocess():
    raw_path = "data/raw/iris.csv"
    processed_path = "data/processed/iris_processed.csv"

    df = pd.read_csv(raw_path)
    # Example: remove nulls (though iris has none)
    df_clean = df.dropna()

    os.makedirs("data/processed", exist_ok=True)
    df_clean.to_csv(processed_path, index=False)
    print(f"Processed data saved to {processed_path}")

if __name__ == "__main__":
    save_raw_data()
    preprocess()