import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", interval="day", count=100)
print(df)