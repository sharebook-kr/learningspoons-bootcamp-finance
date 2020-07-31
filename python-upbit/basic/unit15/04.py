# 목표가 기능 추가 
import pyupbit
import time
import datetime

df = pyupbit.get_ohlcv("KRW-BTC")
yesterday = df.iloc[-2]
today = df.iloc[-1]
yesterday_range = yesterday['high'] - yesterday['low']
target = today['open'] + yesterday_range * 0.5
print("목표가: ", target)

while True: 
    now = datetime.datetime.now()
    price = pyupbit.get_current_price("KRW-BTC")
    print(now, price)
    time.sleep(1)