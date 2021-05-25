# 지정가 매도  
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
})

order = binance.create_limit_sell_order(
    symbol="BTC/USDT",
    amount=0.000999, 
    price =37300 
)

pprint.pprint(order)
