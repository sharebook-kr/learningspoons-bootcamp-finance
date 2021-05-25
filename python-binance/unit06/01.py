# 분붕 조회하기
import ccxt 

binance = ccxt.binance()
btc_ohlcv = binance.fetch_ohlcv("BTC/USDT")
print(btc_ohlcv)