from binance.client import Client

with open("../../binance.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()


client = Client(api_key=api_key, api_secret=api_secret)
balance = client.get_asset_balance(asset='BNB')
print(balance)