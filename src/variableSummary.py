import pandas as pd

sourceFolder = 'Data/processed/'
outFolder = 'Data/processed/'
file = sourceFolder + 'merged_data_2.csv'
df = pd.read_csv(file)
df = df[(df['year'] >= 2010) & (df['year'] <= 2023)]

print(df.head())
print(df.columns)


def variable_summary(df):
    summary = pd.DataFrame({
        'non_missing': df.notna().sum(),
        'missing': df.isna().sum(),
        'nunique': df.nunique()
    })
    return summary


# Whole dataset summary
summary_df = variable_summary(df)
summary_df.to_csv(outFolder + 'variable_summary_all.csv')

# Country by country summary (using 'Code' as the country column)
country_col = 'code'
if country_col in df.columns:
    for country, group in df.groupby(country_col):
        country_summary = variable_summary(group)
        # Clean country name for filename
        country_name = str(country).replace('/', '_').replace(' ', '_')
        country_summary.to_csv(
            f"{outFolder}variable_summary_{country_name}.csv")
else:
    print('No country column named "Code" found for per-country summary.')
