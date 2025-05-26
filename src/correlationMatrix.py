import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def correlation_matrix(inputFile, needPicture=False):
    """
    Computes the correlation matrix for the given CSV file, saves the full correlation matrix as CSV, and plots a heatmap for the top 20 correlations.
    Args:
        inputFile (str): Name of the source CSV file (relative to Data/processed/)
    Returns:
        pd.DataFrame: The full correlation matrix
    """
    sourceFolder = 'Data/processed/'
    outFolder = 'Data/processed/'
    file = sourceFolder + inputFile
    df = pd.read_csv(file)
    df = df[(df['year'] >= 2010) & (df['year'] <= 2023)]

    # 1. Drop country code/year columns
    drop_cols = ['code', 'year']
    df = df.drop(columns=[col for col in drop_cols if col in df.columns])

    # 2. Convert object columns that are actually numbers to numeric
    for col in df.select_dtypes(include='object').columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 3. Now select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    corr_matrix = numeric_df.corr()

    # 4. Find the top 20 correlations
    corr_pairs = corr_matrix.abs().unstack().sort_values(
        kind="quicksort", ascending=False)
    corr_pairs = corr_pairs[corr_pairs < 1]  # Exclude self-correlation
    top_corr = corr_pairs.drop_duplicates().head(20)

    # Save the full correlation matrix to CSV
    corr_matrix.to_csv(outFolder + 'correlation_matrix_all.csv')

    if needPicture:
        # Extract unique variable names from top 20 pairs
        top_vars = set()
        for idx in top_corr.index:
            top_vars.update(idx)
        top_vars = list(top_vars)
        top_corr_matrix = corr_matrix.loc[top_vars, top_vars]

        # 5. Plot heatmap of the top correlations
        sns.set(font_scale=2)
        plt.figure(figsize=(60, 50))
        sns.heatmap(top_corr_matrix, cmap='coolwarm', annot=True, fmt='.2f')
        plt.title('Top Correlations Heatmap')
        plt.tight_layout()
        plt.savefig(outFolder + 'top20_correlation_heatmap.png', dpi=300)
        plt.close()

    return corr_matrix


# Example use case:
# please change file name to your own file
corr_matrix = correlation_matrix('merged_5.csv')
