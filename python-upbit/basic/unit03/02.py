import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", "minute3")
print(df)