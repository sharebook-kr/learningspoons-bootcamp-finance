with open("../account.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()


from binance.client import Client
client = Client(api_key=api_key, api_secret=api_secret)
order = client.order_limit_buy(
    symbol='XRPUSDT',
    quantity=20,
    price=0.89
)
print(order)