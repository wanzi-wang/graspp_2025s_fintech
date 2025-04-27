#All necessary importations
import pandas as pd
import requests
import io
import os

def download_worldbank(indicator, countries, date_start, date_end):
    url_base = 'http://api.worldbank.org/v2/'  # Base URL for the World Bank API
    country_codes = ';'.join(countries)  # Combine country codes into a string
    url = url_base + f'country/{country_codes}/indicator/{indicator}?date={date_start}:{date_end}&per_page=30000' #create the url with start and end date.
    url = url_base + f'country/{country_codes}/indicator/{indicator}?per_page=30000' # This line overrides the previous one. It will ignore start/end date.

    response = requests.get(url)  # Download data from the URL
    df = pd.read_xml(response.content)  # Convert the downloaded data to a table
    return df  # Return the table

#Ok time to test if I can figure out how this works

wb_data = download_worldbank(
    indicator = 'SL.AGR.EMPL.ZS',
    countries = ['IN','VN'],
    date_start = '2021',
    date_end = '2023'
)

wb_data.head(2)