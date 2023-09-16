import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accept': 'application/json',  
    'X-CMC_PRO_API_KEY': '82cb015a-9ff6-4efa-a118-d6e30da02b19'  
}

try:
    response = requests.get(url, params=parameters, headers=headers)
    response.raise_for_status()  
    data = response.json()

    
    print(data['data'][:5])  

   
    pd.set_option('display.max_columns', None)
    
    df = pd.json_normalize(data['data'])  
    print(df.head()) 

except ConnectionError as ce:
    print("Connection Error:", ce)
except Timeout as te:
    print("Timeout Error:", te)
except TooManyRedirects as tme:
    print("Too Many Redirects Error:", tme)
except requests.exceptions.HTTPError as he:
    print("HTTP Error:", he)
except json.JSONDecodeError as jde:
    print("JSON Decode Error:", jde)
except Exception as e:
    print("An error occurred:", e)

