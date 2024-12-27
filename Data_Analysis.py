
import pandas as pd

# Load your dataset
# Replace "data.csv" with your actual dataset file
df = pd.read_csv("data.csv")

# Extract the first five rows
print("First five rows:")
print(df.head(5))

# Extract the last five rows
print("\nLast five rows:")
print(df.tail(5))

# Generate a summary of statistical data
print("\nSummary of statistical data:")
print(df.describe())

# Obtain a data frame summary
print("\nData frame summary:")
print(df.info())

# Check for missing values
print("\nChecking for missing values:")
print(df.isnull().sum())


