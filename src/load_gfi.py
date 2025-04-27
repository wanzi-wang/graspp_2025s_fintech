import pandas as pd

def load_gfi_csv(file_path):
  #Load Global Financial Inclusion India CSV file.
  df=pd.read_csv(file_path)
  return df