from pybit import HTTP
import pprint

with open("../../bybit.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

session = HTTP(
    endpoint="https://api.bybit.com", 
    api_key=api_key, 
    api_secret=api_secret
)

balances = session.get_wallet_balance()
pprint.pprint(balances)