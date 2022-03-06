import ccxt 
import pprint

f = open("../../mexc.key", "r")
lines = f.readlines()
f.close()

api_key = lines[0].strip()
secret = lines[1].strip()
config={'apiKey': api_key, 'secret': secret}

exchange = ccxt.mexc(config=config)
resp = exchange.create_limit_buy_order(
    symbol='XRP/USDT',
    amount=10,
    price=0.5
)
pprint.pprint(resp)