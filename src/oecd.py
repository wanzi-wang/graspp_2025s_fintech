import requests
import pandas as pd

def download_oecd_health(url):
   
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to download OECD data: HTTP {response.status_code}")
    
    df = pd.read_xml(response.content)
    return df
