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
    delta = datetime.timedelta(hours=9)
    ticker_data = { }

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
        row = (dt, code, open, high, low, close,
               acc_volume, acc_price, acc_ask_volume, acc_bid_volume, change_rate)

        try:
            ticker_data[date_utc][code].append(row)
        except KeyError:
            ticker_data[date_utc] = {k:[] for k in krw_tickers}
            ticker_data[date_utc][code].append(row)

        now = datetime.datetime.now()
        print(now, dt, code)

        # save the previous day data to the database
        if now.hour == 9 and now.minute == 10 and (0 <= now.second <=2):
            krw_tickers = pyupbit.get_tickers(fiat="KRW")
            prev_date = (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

            con = sqlite3.connect(f"./{prev_date}-coin.db")
            save_data(con, ticker_data[prev_date])
            con.close()

            del ticker_data[prev_date]
            time.sleep(2.5)