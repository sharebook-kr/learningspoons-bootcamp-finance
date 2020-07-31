# 목표가 기능 추가 
import pyupbit
import time
import datetime

def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return target

target = cal_target("KRW-BTC")
print(target)

while True: 
    now = datetime.datetime.now()
    price = pyupbit.get_current_price("KRW-BTC")
    print(now, price)
    time.sleep(1)