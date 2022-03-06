import ccxt

exchange = ccxt.mexc()
markets = exchange.load_markets()

print(markets.keys())
print(len(markets))

