import requests
import pandas as pd

def download_worldbank(indicators, countries, date_start, date_end):
    
    url_base = 'http://api.worldbank.org/v2/'
    country_codes = ';'.join(countries)
    
    all_data = []
    for indicator in indicators:
        url = url_base + f'country/{country_codes}/indicator/{indicator}?date={date_start}:{date_end}&per_page=30000&format=xml'
        response = requests.get(url)
        df = pd.read_xml(response.content)
        df['indicator_code'] = indicator  # Save indicator code
        all_data.append(df)
    
    combined = pd.concat(all_data, ignore_index=True)
    return combined
