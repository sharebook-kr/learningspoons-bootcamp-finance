import ccxt 
import pprint

with open("../api.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret  = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key, 
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

order = binance.create_limit_sell_order(
    symbol="BTC/USDT",
    amount=0.001, 
    price = 34000 
)

pprint.pprint(order)


