import multiprocessing as mp
import pyupbit
import datetime
import pandas as pd
import sqlite3

DATA_COUNT_MAX = 10000

def save_data(con, ticker_data):
    columns = ['datetime', 'code', 'open', 'high', 'low', 'close',
               'acc_vol', 'acc_price', 'acc_ask_vol', 'acc_bid_vol',
               'change_rate']

    for k, v in ticker_data.items():
        if len(v) !=0:
            df = pd.DataFrame(data=v, columns=columns)
            df.to_sql(name=k, con=con, if_exists='append', index=False, chunksize=1000)


if __name__ == "__main__":
    krw_tickers = pyupbit.get_tickers(fiat="KRW")
    queue = mp.Queue()
    proc = mp.Process(
        target=pyupbit.WebSocketClient,
        args=('ticker', krw_tickers, queue),
        daemon=True
    )
    proc.start()

    now = datetime.datetime.now()
    delta = datetime.timedelta(hours=9)
    now = now - delta
    date = now.strftime("%Y-%m-%d")
    ticker_data = {k:[] for k in krw_tickers}
    data_count = 0
    con = sqlite3.connect(f"./{date}-coin.db")
    prev_date = date

    while True:
        data = queue.get()
        data_count += 1

        code = data['code']
        open = data['opening_price']
        high = data['high_price']
        low  = data['low_price']
        close = data['trade_price']
        ts = data['trade_timestamp']
        acc_volume = data['acc_trade_volume']
        acc_price = data['acc_trade_price']
        acc_ask_volume = data['acc_ask_volume']
        acc_bid_volume = data['acc_bid_volume']
        change_rate = data['signed_change_rate']
        dt = datetime.datetime.fromtimestamp(ts/1000)
        dt_utc = dt - delta
        curr_date = dt_utc.strftime("%Y-%m-%d")

        if (prev_date != curr_date) or (data_count == DATA_COUNT_MAX):
            save_data(con, ticker_data)

            # 날짜 변경 시 새로운 db 열기
            if prev_date != curr_date:
                con = sqlite3.connect(f"./{curr_date}-coin.db")
                krw_tickers = pyupbit.get_tickers(fiat="KRW")       # ticker update

            ticker_data = {k:[] for k in krw_tickers}           # data reset
            data_count = 0

        row = (dt, code, open, high, low, close, acc_volume, acc_price, acc_ask_volume, acc_bid_volume, change_rate)
        ticker_data[code].append(row)
        prev_date = curr_date


