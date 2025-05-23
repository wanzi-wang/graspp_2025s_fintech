import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sourceFolder = 'Data/processed/'
outFolder = 'documents/'
file = sourceFolder + 'merged_data_2.csv'
df = pd.read_csv(file)
df = df[(df['year'] >= 2010) & (df['year'] <= 2023)]

print(df.head())
print(df.columns)


# # raise ValueError("Your error message here")
# numeric_df = df.select_dtypes(include='number')

# # 1. Dropped non-numeric columns
# all_columns = set(df.columns)
# numeric_columns = set(numeric_df.columns)
# dropped_non_numeric = list(all_columns - numeric_columns)
# # print("Dropped non-numeric columns:", dropped_non_numeric)
# myFile = outFolder + 'dropped_non_numeric.txt'
# with open(myFile, 'w') as f:
#     for item in dropped_non_numeric:
#         f.write(f"{item}\n")

# # Remove rows and columns with all NaN or infinite values
# corr = numeric_df.corr()
# corr = corr.replace([np.inf, -np.inf], np.nan).dropna(axis=0,
#                                                       how='all').dropna(axis=1, how='all')

# # 2. Dropped columns with all NaN or infinite correlations
# final_columns = set(corr.columns)
# dropped_corr_columns = list(numeric_columns - final_columns)
# # print("Dropped columns with all NaN or infinite correlations:", dropped_corr_columns)
# file = outFolder + 'dropped_corr_columns.txt'
# with open(file, 'w') as f:
#     for item in dropped_corr_columns:
#         f.write(f"{item}\n")

# sns.clustermap(corr, cmap='coolwarm', figsize=(20, 20))
# # plt.show()
# heatmap = outFolder + 'correlation_heatmap.png'
# plt.savefig(heatmap, dpi=300, bbox_inches='tight')


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
