import ccxt
import pprint

f = open("../../bitget.key", "r")
lines = f.readlines()
f.close()

api_key = lines[0].strip()
secret = lines[1].strip()
config={'apiKey': api_key, 'secret': secret}

exchange = ccxt.bitget(config=config)
balance = exchange.fetch_balance()
pprint.pprint(balance)