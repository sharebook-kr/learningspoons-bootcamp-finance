import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", "minute5")
print(df)