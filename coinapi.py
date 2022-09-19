import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

sym = "BTC"

url = f"https://rest.coinapi.io/v1/exchangerate/{sym}/USD"

# url = "https://rest.coinapi.io/v1/exchanges/"

headers = {'X-CoinAPI-Key' : os.getenv('COIN_API_KEY')}

params = {  
    "time": "2019-04-15T22:42:21.3763342Z"
}

response = requests.get(url, headers=headers, params=params)

# response = requests.get(url, headers=headers)
if response.status_code == 200: 
    print("response")
data = response.json()

print(data)

print("{:.2f}".format(data["rate"]))

