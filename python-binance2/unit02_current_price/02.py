import time
import datetime
from binance.client import Client

with open("../../binance.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

client = Client(api_key=api_key, api_secret=api_secret)

while True:
    btc = client.get_symbol_ticker(symbol="BTCUSDT")
    now = datetime.datetime.now()
    price = btc['price']
    print(now, price)
    time.sleep(1)
