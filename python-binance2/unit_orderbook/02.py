import pprint

with open("../account.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()


from binance.client import Client
client = Client(api_key=api_key, api_secret=api_secret)
orderbook = client.get_order_book(symbol="BTCUSDT")
asks = orderbook['asks']
bids = orderbook['bids']

pprint.pprint(asks)
pprint.pprint(bids)