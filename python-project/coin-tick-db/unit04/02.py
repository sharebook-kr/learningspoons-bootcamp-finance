import multiprocessing as mp
import pyupbit
import datetime
import pandas as pd
import sqlite3
import time
import threading
import logging
import logging.handlers


# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

file_handler = logging.handlers.TimedRotatingFileHandler(filename="log", when = "H", interval=1)
file_handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def save_data(con, ticker_data):
    columns = ['datetime', 'code', 'price', 'volume']
    for k, v in ticker_data.items():
        if len(v) !=0:
            df = pd.DataFrame(data=v, columns=columns)
            df.to_sql(name=k, con=con, if_exists='append', index=False, chunksize=1000)


class Worker(threading.Thread):
    def __init__(self, data, lock):
        super().__init__()
        self.data = data
        self.lock = lock

    def run(self):
        while True:
            now = datetime.datetime.now()
            logger.info("Worker thread true")

            if now.hour == 9 and now.minute == 30 and (0 <= now.second <=3):
                with self.lock:
                    yesterday = (now - datetime.timedelta(days=1))
                    date = yesterday.strftime("%Y-%m-%d")
                    con = sqlite3.connect(f"./{date}-coin.db")
                    save_data(con, self.data[date])
                    con.close()
                    del self.data[date]
                    time.sleep(3)
            else:
                time.sleep(1)


if __name__ == "__main__":
    # tickers
    krw_tickers = pyupbit.get_tickers(fiat="KRW")

    # queue and sub process
    queue = mp.Queue()
    proc = mp.Process(
        target=pyupbit.WebSocketClient,
        args=('trade', krw_tickers, queue),
        daemon=True
    )
    proc.start()

    # main process
    delta = datetime.timedelta(hours=9)
    ticker_data = { }

    # SubThread
    lock = threading.Lock()
    w = Worker(ticker_data, lock)
    w.start()

    while True:
        data = queue.get()

        try:
            code = data['code']
            price = data['trade_price']
            volume = data['trade_volume']
            ts = data['trade_timestamp']
        except Exception as e:
            print(e)
            continue

        # save data
        dt = datetime.datetime.fromtimestamp(ts/1000)
        dt_utc = dt - delta
        date_utc = dt_utc.strftime("%Y-%m-%d")
        row = (dt, code, price, volume)

        # acquire the lock
        with lock:
            try:
                ticker_data[date_utc][code].append(row)
            except KeyError:
                ticker_data[date_utc] = {k:[] for k in krw_tickers}
                ticker_data[date_utc][code].append(row)
