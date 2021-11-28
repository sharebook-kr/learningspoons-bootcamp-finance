f = open("../account.txt")
lines = f.readlines()
f.close()
api_key = lines[0].strip()
api_secret = lines[1].strip()


from binance.client import Client
client = Client(api_key=api_key, api_secret=api_secret)
tickers = client.get_all_tickers()

for ticker in tickers:
    symbol = ticker['symbol']
    if 'BTC' in symbol:
        print(symbol)