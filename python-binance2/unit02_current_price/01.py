with open("../account.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

from binance.client import Client
client = Client(api_key=api_key, api_secret=api_secret)
btc_usdt = client.get_symbol_ticker(symbol="BTCUSDT")
print(btc_usdt)