import pyupbit
import time
import datetime

DELAY = 0.2           
TS_MARGIN = 0.80      # 고점 대비 20% 하락시 매도 

with open("account.txt") as f:
    lines = f.readlines()
    access = lines[0].strip()
    secret = lines[1].strip()
    print(access, secret)

# 원화 잔고 조회
upbit = pyupbit.Upbit(access, secret)
krw_balance = upbit.get_balance(ticker="KRW")

prev_tickers = pyupbit.get_tickers()
time.sleep(DELAY)

while True:
    now = datetime.datetime.now()
    curr_tickers = pyupbit.get_tickers()
    diff_set = set(curr_tickers) - set(prev_tickers)

    if len(diff_set) == 0:
        print(now, "업비트 신규 상장 감시 중 ...")
        time.sleep(DELAY)
        continue
    else:
        ticker = diff_set.pop()
        print("신규 상장: ", ticker)

        # 신규상장 암호화폐 시장가 매수
        upbit.buy_market_order(ticker, krw_balance)
        time.sleep(DELAY)

        coin_balance = upbit.get_balance(ticker)
        high_price = pyupbit.get_current_price(ticker)
        time.sleep(DELAY)

        while True:
            curr_price = pyupbit.get_current_price(ticker)

            # Trailing stop
            if (curr_price < (high_price * TS_MARGIN)):
                # 고점대비 설정값 만큼 하락시 매도 
                upbit.sell_market_order(ticker, coin_balance)
                break

            high_price = max(high_price, curr_price)
            time.sleep(DELAY)
        
        # 바깥 while loop로 이동  
        continue


