# src/load_and_clean.py

import pandas as pd

def load_raw_data('../data/raw/global_financial_inclusion_india.csv'):
    """Load raw CSV file."""
    return pd.read_csv('../data/raw/global_financial_inclusion_india.csv')

def basic_cleaning(df):
    """Simple cleaning: drop rows with all missing values."""
    df_clean = df.dropna(how='all')
    return df_clean

def save_processed_data(df, output_path):
    """Save cleaned data to processed folder."""
    df.to_csv(output_path, index=False)