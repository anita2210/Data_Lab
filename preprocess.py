import pandas as pd

# Column names for the Adult Income dataset (no header in the raw file)
columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education_num',
    'marital_status', 'occupation', 'relationship', 'race', 'sex',
    'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income'
]

df = pd.read_csv('data/adult_income.csv', header=None, names=columns)

# Strip whitespace from string columns (values are padded with spaces)
df = df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)

print(f"V1 shape: {df.shape}")

# V2: Remove rows where 'workclass', 'occupation', or 'native_country' are unknown ('?')
df_cleaned = df[
    (df['workclass'] != '?') &
    (df['occupation'] != '?') &
    (df['native_country'] != '?')
]

print(f"V2 shape after cleaning: {df_cleaned.shape}")

df_cleaned.to_csv('data/adult_income.csv', index=False)
print("Saved cleaned dataset!")