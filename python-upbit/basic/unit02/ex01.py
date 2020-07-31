import pyupbit

btc_tickers = pyupbit.get_tickers(fiat="BTC")
print(btc_tickers)
print(len(btc_tickers))