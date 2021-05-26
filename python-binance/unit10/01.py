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

order = binance.create_limit_buy_order(
    symbol="BTC/USDT",
    amount=0.01, 
    price = 20000
)

pprint.pprint(order)


