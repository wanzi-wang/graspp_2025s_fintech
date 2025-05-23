import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sourceFolder = 'Data/processed/'
outFolder = 'Data/processed/'
file = sourceFolder + 'merged_data_2.csv'
df = pd.read_csv(file)
df = df[(df['year'] >= 2010) & (df['year'] <= 2023)]

print(df.head())
print(df.columns)

# 1. Drop country code/year columns
drop_cols = ['code', 'year']
df = df.drop(columns=[col for col in drop_cols if col in df.columns])

# 2. Convert object columns that are actually numbers to numeric
for col in df.select_dtypes(include='object').columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 3. Now select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['int64', 'float64'])
corr = numeric_df.corr()

# 4. Find the top 20 correlations
corr_matrix = numeric_df.corr()
corr_pairs = corr_matrix.abs().unstack().sort_values(
    kind="quicksort", ascending=False)
corr_pairs = corr_pairs[corr_pairs < 1]  # Exclude self-correlation
top_corr = corr_pairs.drop_duplicates().head(20)

# Save the full correlation matrix to CSV
corr_matrix.to_csv(outFolder + 'correlation_matrix_all.csv')

# Extract unique variable names from top 20 pairs
top_vars = set()
for idx in top_corr.index:
    top_vars.update(idx)

# Create a submatrix for these variables
top_vars = list(top_vars)
top_corr_matrix = corr_matrix.loc[top_vars, top_vars]

# 5. Plot heatmap of the top correlations
# Increase all font sizes (axis labels, tick labels, etc.)
sns.set(font_scale=2)
plt.figure(figsize=(60, 50))
sns.heatmap(top_corr_matrix, cmap='coolwarm', annot=True, fmt='.2f')
plt.title('Top Correlations Heatmap')
plt.tight_layout()
plt.savefig(outFolder + 'top20_correlation_heatmap.png', dpi=300)
plt.close()
