import pyupbit

tickers = pyupbit.get_tickers()
print(tickers)
print(len(tickers))