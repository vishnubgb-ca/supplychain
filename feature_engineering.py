import pandas as pd

# Load data from csv file
df = pd.read_csv('data.csv')

# Check if 'AGE' column exists in the dataframe
if 'AGE' in df.columns:
    # Delete 'AGE' column
    df = df.drop('AGE', axis=1)

# Check for duplicate rows
duplicates = df.duplicated()
if duplicates.any():
    # Delete duplicate rows
    df = df.drop_duplicates()

# Check if 'ICU' column exists in the dataframe
if 'ICU' in df.columns:
    # Delete 'ICU' column
    df = df.drop('ICU', axis=1)

# Save the cleaned dataframe to a csv file
df.to_csv('cleaned_data.csv', index=False)

# Print the top 5 rows of the cleaned dataframe
print(df.head(5))