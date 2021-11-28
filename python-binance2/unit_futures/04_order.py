with open("../account.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()


from binance.client import Client
client = Client(api_key=api_key, api_secret=api_secret)
order = client.futures_create_order(
    symbol="XRPUSDT",
    type="LIMIT",
    timeInForce='GTC',
    price=0.85,
    side='BUY',
    quantity=10
)
print(order)