import pandas as pd
import numpy as np

# Load the dataset (change this to the correct path of your CSV file)
df = pd.read_csv("dataowid-covid-data.csv")

# Print column names
print("Columns in the dataset:")
print(df.columns)

# Check for missing values (nulls)
print("\nMissing values in each column:")
print(df.isnull().sum())

# Replace "null" strings with NaN (if needed)
df.replace("null", np.nan, inplace=True)

# Recheck for missing values after replacement
print("\nMissing values after replacing 'null' with NaN:")
print(df.isnull().sum())

# Display basic statistics of the numerical columns
print("\nBasic statistics of numerical columns:")
print(df.describe())
