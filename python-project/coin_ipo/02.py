import pyupbit
import time

DELAY = 0.2

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
    curr_tickers = pyupbit.get_tickers()
    diff_set = set(curr_tickers) - set(prev_tickers)

    if len(diff_set) == 0:
        time.sleep(DELAY)
        continue
    else:
        ticker = diff_set.pop()
        # 신규상장 암호화폐 시장가 매수
        upbit.buy_market_order(ticker, krw_balance)