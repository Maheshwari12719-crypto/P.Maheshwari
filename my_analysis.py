import pandas as pd
from pathlib import Path

# Get the folder where this Python file is located
BASE_DIR = Path(__file__).resolve().parent

# Load the dataset
file_path = BASE_DIR / "data" / "ecommerce_user_events.csv"

df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nEvent types:")
print(df["event_type"].value_counts())
print("\nMissing values:")
print(df.isnull().sum())