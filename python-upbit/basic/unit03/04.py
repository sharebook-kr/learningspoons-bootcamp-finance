import pyupbit
import pandas as pd

df = pyupbit.get_ohlcv("KRW-BTC", "minute1")
print(df)

df1 = df['open'].resample('3T').first()
df2 = df['high'].resample('3T').max()
df3 = df['low'].resample('3T').min()
df4 = df['close'].resample('3T').last()
df5 = df['volume'].resample('3T').sum()

df = pd.concat([df1, df2, df3, df4, df5], axis=1)
print(df)
