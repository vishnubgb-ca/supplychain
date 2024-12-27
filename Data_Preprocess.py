
import pandas as pd

# Assuming df is your DataFrame
df =pd.read_csv("data.csv")
df = df.dropna()  # remove missing values
df = df.drop_duplicates()  # remove duplicate rows
df.to_csv("data.csv")
print(df)

