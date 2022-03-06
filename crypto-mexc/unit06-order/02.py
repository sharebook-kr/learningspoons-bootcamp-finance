import ccxt 
import pprint

f = open("../../mexc.key", "r")
lines = f.readlines()
f.close()

api_key = lines[0].strip()
secret = lines[1].strip()
config={'apiKey': api_key, 'secret': secret}

exchange = ccxt.mexc(config=config)
id = '5367995674094924a94f4646c42b3f67'
resp = exchange.cancel_order(id=id, symbol='XRP/USDT')
pprint.pprint(resp)