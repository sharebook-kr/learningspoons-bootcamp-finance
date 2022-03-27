import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import * 
import pyupbit 
import math
import datetime
import numpy as np

def calculate_rsi(df):
    df['변화량'] = df['close'] - df['close'].shift(1)
    df['상승폭'] = np.where(df['변화량']>=0, df['변화량'], 0)
    df['하락폭'] = np.where(df['변화량'] <0, df['변화량'].abs(), 0)

    # welles moving average
    df['AU'] = df['상승폭'].ewm(alpha=1/14, min_periods=14).mean()
    df['AD'] = df['하락폭'].ewm(alpha=1/14, min_periods=14).mean()
    df['RSI'] = df['AU'] / (df['AU'] + df['AD']) * 100
    return df.iloc[-1]['RSI']


class Worker(QThread):
    # user signal
    rsi_calculate_done = pyqtSignal(dict)
    progress = pyqtSignal(float)

    def __init__(self):
        super().__init__()
        
    def run(self):
        krw_tickers = pyupbit.get_tickers(fiat="KRW")

        result = {}
        for i, ticker in enumerate(krw_tickers):
            df = pyupbit.get_ohlcv(ticker)
            rsi = calculate_rsi(df)
            result[ticker] = rsi

            # 진행 정도 emit
            percent = (i + 1) * 100 / len(krw_tickers)
            self.progress.emit(percent)

            # sleep
            self.msleep(100)         # 0.1 secs

        # 최종 rsi emit
        self.rsi_calculate_done.emit(result)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # variables
        self.percent = 0

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("업비트 현재가 및 RSI v1.0")
        self.create_table_widget()

        # timer 
        self.timer_price = QTimer(self)
        self.timer_price.start(1000)
        self.timer_price.timeout.connect(self.update_price)

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.table_widget)
        self.setCentralWidget(widget)

        # thread 
        self.worker = Worker()
        self.worker.start()
        self.worker.rsi_calculate_done.connect(self.update_rsi)
        self.worker.progress.connect(self.update_progress)

    @pyqtSlot(float)
    def update_progress(self, percent):
        self.percent = percent 


    def create_table_widget(self):
        krw_tickers = pyupbit.get_tickers(fiat="KRW")

        self.table_widget = QTableWidget()
        labels = ['ticker', 'name', 'price', 'RSI']
        #self.table_widget.setSortingEnabled(True)
        self.table_widget.setColumnCount(len(labels))
        self.table_widget.setRowCount(len(krw_tickers))
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setHorizontalHeaderLabels(labels)
        self.update_price()

    def query_price(self, tickers):
        hundred = math.ceil(len(tickers) / 100)        # 110 -> 2

        result = {}
        for i in range(hundred):
            tickers100 = tickers[100*i:100*i+100]
            cur_price = pyupbit.get_current_price(tickers100)
            result.update(cur_price)

        return result

    def update_price(self):
        now = datetime.datetime.now()
        now = str(now)[:19]
        fmt = f"현재시간: {now} | RSI 계산 {self.percent:.2f} % 완료"
        self.statusBar().showMessage(fmt)

        ticker_name = pyupbit.get_tickers(fiat="KRW", verbose=True)
        krw_tickers = pyupbit.get_tickers(fiat="KRW")
        self.table_widget.setRowCount(len(krw_tickers))
        price = self.query_price(krw_tickers)

        row = 0
        for ticker, cur_price in price.items():
            item = QTableWidgetItem(ticker)
            item.setTextAlignment(int(Qt.AlignCenter|Qt.AlignVCenter))
            self.table_widget.setItem(row, 0, item) 

            # name
            name = ticker_name[row]['korean_name']
            item = QTableWidgetItem(name)
            item.setTextAlignment(int(Qt.AlignCenter|Qt.AlignVCenter))
            self.table_widget.setItem(row, 1, item) 

            #item = QTableWidgetItem()
            #item.setData(Qt.DisplayRole, int(cur_price))
            item = QTableWidgetItem(format(cur_price, ","))
            item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
            self.table_widget.setItem(row, 2, item) 
            row += 1

    @pyqtSlot(dict)
    def update_rsi(self, data):
        row = 0
        for ticker, rsi in data.items():
            #item = QTableWidgetItem()
            #item.setData(Qt.DisplayRole, float(rsi))
            item = QTableWidgetItem(f"{rsi:.2f}")
            item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
            self.table_widget.setItem(row, 3, item) 
            row += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()