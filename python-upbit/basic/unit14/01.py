import pyupbit

df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="day", count=200)
df.to_excel("BTC.xlsx")