import ccxt

exchange = ccxt.mexc()
orderbook = exchange.fetch_order_book('ETH/USDT')
print(orderbook['asks'])
print(orderbook['bids'])