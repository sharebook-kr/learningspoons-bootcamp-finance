import pyupbit

df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="week")
print(df)