import pyupbit
import time
import datetime

tickers = pyupbit.get_tickers()
ticker = input("조회할 가상화폐 티커를 입력하세요: ")
if ticker not in tickers:
    print("지원하지 않는 가상화폐입니다.")
else:
    print("===== 조회를 시작합니다. =====")

    while True:
        price = pyupbit.get_current_price(ticker)
        time.sleep(1)
        now = datetime.datetime.now()
        print(now, price)
