# 예외처리 
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

    # 8시 59분 50초 ~ 09:00:00 초 사이에 매도 
    if now.hour == 8 and now.minute == 59 and (50 <= now.second <= 59):
        if op_mode is True and hold is True:
            btc_balance = upbit.get_balance("KRW-BTC")
            upbit.sell_market_order("KRW-BTC", btc_balance)
            hold = False

        # 새로운 거래일에서 목표가 갱신될 때 까지 거래가 되지 않도록
        op_mode = False
        time.sleep(10)

    # 9시 0분 20초 ~ 30초 사이에 
    if now.hour == 9 and now.minute == 0 and (20 <= now.second <= 30):
        target = cal_target("KRW-BTC")
        op_mode = True

    price = pyupbit.get_current_price("KRW-BTC")

    # 매수시도 
    if op_mode is True and price is not None and price >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")
        upbit.buy_market_order("KRW-BTC", krw_balance)
        hold = True

    # 상태 출력 
    print(f"현재시간 {now} 목표가: {target} 현재가: {price} 보유상태: {hold} 동작상태: {op_mode}")
    
    time.sleep(1)

