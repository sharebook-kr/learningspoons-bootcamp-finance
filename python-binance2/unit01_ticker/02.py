from tkinter import W
from binance.client import Client

f = open("../../binance.key")
lines = f.readlines()
f.close()
api_key = lines[0].strip()
api_secret = lines[1].strip()


client = Client(api_key=api_key, api_secret=api_secret)
tickers = client.get_all_tickers()

for i,ticker in enumerate(tickers):
    symbol = ticker['symbol']
    price = float(ticker['price'])
    if 'BTCUSDT' in symbol:
        print(f"{i: 4}", f"{symbol:16}", f"{price:20.8f}")