import pandas as pd

# Load data from csv file
df = pd.read_csv('data.csv')

# Check if 'AGE' column exists in the dataframe
if 'AGE' in df.columns:
    # Drop 'AGE' column from the dataframe
    df = df.drop('AGE', axis=1)
else:
    print("'AGE' column not found in the dataframe.")

# Handle NaN values
df = df.dropna()

# Save the cleaned dataframe to a new csv file
df.to_csv('cleaned_data.csv', index=False)

# Print the top 5 rows of the cleaned dataframe
print(df.head(5))