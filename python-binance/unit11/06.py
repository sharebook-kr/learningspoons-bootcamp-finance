# 보유 포지션 조회
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

balance = binance.fetch_balance()
positions = balance['info']['positions']

for position in positions:
    if position["symbol"] == "BTCUSDT":
        pprint.pprint(position)

