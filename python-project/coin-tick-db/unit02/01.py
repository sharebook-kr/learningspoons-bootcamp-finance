import pyupbit

tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)
print(len(tickers))