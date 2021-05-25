import ccxt 

binance = ccxt.binance()            # 바이낸스 객체 생성
markets = binance.load_markets()    # 티커

print(markets.keys())
print(len(markets))