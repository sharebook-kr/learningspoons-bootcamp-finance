# 대기 주문 조회 
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

open_orders = binance.fetch_open_orders(
    symbol="BTC/USDT"
)
pprint.pprint(open_orders)

