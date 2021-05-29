# 선물 호가(오더북, OrderBook) 조회
import ccxt 

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

orderbook = binance.fetch_order_book("BTC/USDT")
asks = orderbook['asks']        # 매도호가 500개
bids = orderbook['bids']        # 매수호가 500개
print(asks[0])
print(bids[0])
