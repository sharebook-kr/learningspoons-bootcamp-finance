import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
unix_time = [x.timestamp() for x in df.index]
print(unix_time)
print(type(df.index[0]))