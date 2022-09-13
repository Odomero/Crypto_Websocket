import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

s = "ETH"
symbol = f"BITSTAMP_SPOT_{s}_USD"
print(symbol)

url = f"https://rest.coinapi.io/v1/trades/{symbol}/history"

# url = "https://rest.coinapi.io/v1/exchanges/"

headers = {'X-CoinAPI-Key' : os.getenv('COIN_API_KEY')}

params = {  
    "time_start": "2019-03-18T22:42:21.3763342Z",
    "limit": 1
}

response = requests.get(url, headers=headers, params=params)

# response = requests.get(url, headers=headers)

data = response.json()

print(data[0]["price"])

