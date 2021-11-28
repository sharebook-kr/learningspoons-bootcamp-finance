with open("../account.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()


from binance.client import Client
client = Client(api_key=api_key, api_secret=api_secret)
result = client.cancel_order(
    symbol="XRPUSDT",
    orderId=3665527812)
print(result)