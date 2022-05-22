import ccxt

exchange = ccxt.bitget()
markets = exchange.load_markets()    # 티커

print(markets.keys())
print(len(markets))