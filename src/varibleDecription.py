import pandas as pd

sourceFolder = 'Data/processed/'
outFolder = 'Data/processed/'
file = sourceFolder + 'merged_data_2.csv'
df = pd.read_csv(file)
df = df[(df['year'] >= 2010) & (df['year'] <= 2025)]

# Convert object columns that are actually numbers to numeric
for col in df.select_dtypes(include='object').columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')


# create summary stats for all the varialbe
df_summary = df.describe()
df_summary.to_csv(outFolder + 'variableDescription.csv')
