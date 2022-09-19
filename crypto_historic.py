import os
import requests
import json
from dotenv import load_dotenv


url = "https://data.alpaca.markets/v1beta2/crypto/bars"


payload = {
            "symbols": ["BTC/USD"],
            "timeframe": "1Hour",
            "start": "2021-05-09",
            "end": "2021-05-09",
            "limit":10
        }

response = requests.get(url,params=payload)

print(response.json())