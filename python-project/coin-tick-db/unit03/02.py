import multiprocessing as mp
import pyupbit
import datetime
import pandas as pd
import sqlite3


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

    ticker_data = {k:[] for k in krw_tickers}
    data_count = 0
    data_count_max = 10000
    con = sqlite3.connect("./2022-06-29-coin.db")

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
        row = (dt, code, open, high, low, close, acc_volume, acc_price, acc_ask_volume, acc_bid_volume, change_rate)
        ticker_data[code].append(row)

        print(data_count)
        if data_count == data_count_max:
            print("*" * 80)
            save_data(con, ticker_data)
            ticker_data = {k:[] for k in krw_tickers}
            data_count = 0


