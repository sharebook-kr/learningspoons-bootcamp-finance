import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", "minute1")
print(df)