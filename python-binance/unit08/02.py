# 주문 취소 
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

resp = binance.cancel_order(
    id = "6141637114",          # 주문 아이디
    symbol="BTC/USDT",
)

pprint.pprint(resp)
