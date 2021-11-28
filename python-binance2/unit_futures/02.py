with open("../account.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()


from binance.client import Client
client = Client(api_key=api_key, api_secret=api_secret)
data = client.futures_historical_klines(
    symbol="BTCUSDT",
    interval='1d',
    start_str='2021-01-01',
    end_str="2021-11-26"
)
print(data)