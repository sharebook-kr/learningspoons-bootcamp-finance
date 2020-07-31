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

# 객체 생성
f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access, secret)

target = cal_target("KRW-BTC")
op_mode = False
hold = False


while True: 
    now = datetime.datetime.now()

    # 9시 0분 20초 ~ 30초 사이에 
    if now.hour == 9 and now.minute == 0 and (20 <= now.second <= 30):
        target = cal_target("KRW-BTC")
        op_mode = True

    price = pyupbit.get_current_price("KRW-BTC")
    print(now, price)


    # 매수시도 
    if op_mode is True and price >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")
        upbit.buy_market_order("KRW-BTC", krw_balance)
        hold = True

    time.sleep(1)

