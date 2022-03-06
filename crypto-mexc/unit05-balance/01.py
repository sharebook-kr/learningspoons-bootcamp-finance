import ccxt 

f = open("../../mexc.key", "r")
lines = f.readlines()
f.close()

api_key = lines[0].strip()
secret = lines[1].strip()
config={'apiKey': api_key, 'secret': secret}

exchange = ccxt.mexc(config=config)
balance = exchange.fetch_balance()
print(balance['MX'])