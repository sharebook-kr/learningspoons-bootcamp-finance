# 티커를 소문자로 입력해도 정상적으로 인식하도록
import pyupbit
import time
import datetime

tickers = pyupbit.get_tickers()
user_ticker = input("조회하고 싶은 티커를 입력해주세요: ")
user_ticker = user_ticker.upper()

if user_ticker not in tickers:
    print("지원하지 않는 티커입니다.")
else:
    print("===== 조회를 시작합니다. =====")

    # 1초에 한 번 가상화폐를 조회하는 코드 
    while True:
        price = pyupbit.get_current_price(user_ticker)
        now = datetime.datetime.now()
        print(now, price)
        time.sleep(1)
