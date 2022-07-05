import multiprocessing as mp
import pyupbit
import datetime
import pandas as pd
import sqlite3
import time

def save_data(con, ticker_data):
    columns = ['datetime', 'code', 'open', 'high', 'low', 'close',
               'acc_vol', 'acc_price', 'acc_ask_vol', 'acc_bid_vol',
               'change_rate']

    for k, v in ticker_data.items():
        if len(v) !=0:
            df = pd.DataFrame(data=v, columns=columns)
            df.to_sql(name=k, con=con, if_exists='append', index=False, chunksize=1000)


if __name__ == "__main__":
    # tickers
    krw_tickers = pyupbit.get_tickers(fiat="KRW")

    # queue and sub process
    queue = mp.Queue()
    proc = mp.Process(
        target=pyupbit.WebSocketClient,
        args=('ticker', krw_tickers, queue),
        daemon=True
    )
    proc.start()

    # main process
    now = datetime.datetime.now()
    delta = datetime.timedelta(hours=9)
    now = now - delta
    date = now.strftime("%Y-%m-%d")         # "2022-07-05"
    ticker_data = {date: {k:[] for k in krw_tickers} }
    cons = {date: sqlite3.connect(f"./{date}-coin.db")}

    while True:
        data = queue.get()

        try:
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
        except Exception as e:
            print(e)
            continue

        # save data
        dt = datetime.datetime.fromtimestamp(ts/1000)
        dt_utc = dt - delta
        date_utc = dt_utc.strftime("%Y-%m-%d")
        row = (dt, code, open, high, low, close, acc_volume, acc_price, acc_ask_volume, acc_bid_volume, change_rate)
        ticker_data[date_utc][code].append(row)

        now = datetime.datetime.now()

        # the next day
        if now.hour == 8 and now.minute == 50 and (0 <= now.second <=2):
            krw_tickers = pyupbit.get_tickers(fiat="KRW")
            next_date = now.strftime("%Y-%m-%d")
            ticker_data[next_date] = {k:[] for k in krw_tickers}
            cons[next_date] = sqlite3.connect(f"./{next_date}-coin.db")
            time.sleep(2.5)

        # save the previous day data to the database
        if now.hour == 9 and now.minute == 10 and (0 <= now.second <=2):
            prev_date = (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            save_data(cons[prev_date], ticker_data[prev_date])
            del cons[prev_date]
            del ticker_data[prev_date]
            time.sleep(2.5)