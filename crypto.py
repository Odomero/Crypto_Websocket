from alpaca_trade_api.stream import Stream
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "wss://stream.data.alpaca.markets/v1beta2/crypto"
data_feed = "iex" 

stream = Stream(os.getenv('API_KEY'),
                os.getenv('API_SECRET'),
                base_url=base_url,
                data_feed=data_feed)

async def bar_callback(b):
    print(b)

# Subscribing to bar event
symbol = ["BTCUSD", "ETHUSD"]
stream.subscribe_crypto_trades(bar_callback, *symbol)

stream.run()