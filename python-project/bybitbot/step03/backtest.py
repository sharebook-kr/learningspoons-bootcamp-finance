from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pybit import HTTP
import datetime
import time
import pandas as pd
import numpy as np


class BackTest(QThread):
    params = pyqtSignal(list)

    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol 
        self.df = None
        self.session = HTTP(
            endpoint="https://api.bybit.com",
            spot=False
        )

    def fetch_days(self):
        now = datetime.datetime.now()
        today = datetime.datetime(
            year=now.year,
            month=now.month,
            day=now.day,
            hour=0,
            minute=0,
            second=0
        )

        delta = datetime.timedelta(days=-60)
        dt = today + delta 
        from_time = time.mktime(dt.timetuple())

        resp = self.session.query_kline(
            symbol=self.symbol,
            interval="D",
            limit=60,
            from_time=from_time
        )

        result = resp['result']
        df = pd.DataFrame(result)
        ts = pd.to_datetime(df['open_time'], unit='s')
        df.set_index(ts, inplace=True)
        return df[['open', 'high', 'low', 'close']]

    @staticmethod
    def backtest(df, window, k):
        df['ma'] = df['close'].rolling(window=window).mean().shift(1)
        df['range'] = (df['high'] - df['low']) * k
        df['target'] = df['open'] + df['range'].shift(1)    # 전일 range * k

        # 상승장/하락장 
        df['status'] = df['open'] > df['ma']

        df['수익률'] = np.where(
            (df['high'] > df['target']) & (df['status']), 
            df['close'] / df['target'], 
            1
        )

        df['누적수익률'] = df['수익률'].cumprod()
        return df['누적수익률'][-1]

    def find_optimal(self, df):
        best_return = 0
        best_window = 0
        best_k = 0

        for window in range(5, 21):
            for k in np.arange(0.3, 0.7, 0.01):
                cur_return = self.backtest(df, window, k)

                if cur_return > best_return:
                    best_return = cur_return
                    best_window = window 
                    best_k = k

        return (best_window, best_k)

    def run(self):
        df = self.fetch_days()
        window, k = self.find_optimal(df)
        self.params.emit([self.symbol, window, k])
