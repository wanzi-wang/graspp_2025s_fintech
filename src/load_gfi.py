import pandas as pd

def load_gfi_csv('../data/raw/global_financial_inclusion_india.csv'):
  #Load Global Financial Inclusion India CSV file.
  df=pd.read_csv('../data/raw/global_financial_inclusion_india.csv')
  return df
