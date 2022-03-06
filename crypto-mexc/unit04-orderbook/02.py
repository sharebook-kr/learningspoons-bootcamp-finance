import ccxt

exchange = ccxt.mexc()
orderbook = exchange.fetch_order_book('BTC/USDT')
asks = orderbook['asks']

for ask in asks:
    print(ask[0], ask[1])