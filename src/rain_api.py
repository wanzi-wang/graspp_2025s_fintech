import requests
import pandas as pd

# API endpoint
url="https://climateknowledgeportal.worldbank.org/extremes/rx5day/median/annual/all/aep100mm/ssp119/historical/subnationals/IND,IND.1151,IND.1152,IND.1153,IND.1154,IND.1155,IND.1156,IND.1157,IND.1158,IND.1159,IND.11510,IND.11511,IND.11512,IND.11513,IND.11514,IND.11515,IND.11516,IND.11517,IND.11518,IND.11519,IND.11520,IND.11521,IND.11522,IND.11523,IND.11524,IND.11525,IND.11526,IND.11527,IND.11528,IND.11529,IND.11530,IND.11531,IND.11532,IND.11533,IND.11534,IND.11535,IND.11536?_format=json"

# Fetch data
response = requests.get(url)

# Raise error if the request failed
response.raise_for_status()

# Convert JSON to Python object
data = response.json()

# Convert to DataFrame
df = pd.json_normalize(data)

# Display or save
print(df.head())

# Optional: save to CSV
df.to_csv("data_raw/rx5day_india_ssp119.csv", index=False)
