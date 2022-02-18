import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import finplot as fplt
from matplotlib.axis import YAxis
import pyupbit
import datetime
import time
import pandas as pd

fplt.display_timezone = datetime.timezone.utc 
fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000" 
fplt.candle_bear_color = "#0000FF"


class Worker(QThread):
    timeout = pyqtSignal(pd.DataFrame)

    def __init__(self):
        super().__init__()
    
    def get_ohlcv(self):
        self.df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="minute1")
        self.df = self.df[['open', 'high', 'low', 'close']]
        self.df.columns = ['Open', 'High', 'Low', 'Close']

    def run(self):
        self.get_ohlcv()
        while True:
            data = pyupbit.get_current_price("KRW-BTC", verbose=True)
            price = data['trade_price']
            timestamp = data['trade_timestamp'] / 1000
            cur_min_timestamp = timestamp - timestamp % (60)
            cur_min_dt = datetime.datetime.fromtimestamp(cur_min_timestamp)

            if cur_min_dt > self.df.index[-1]:
                self.get_ohlcv()
            else:
                # update last candle
                self.df.iloc[-1]['Close'] = price 
                if price > self.df.iloc[-1]['High']:
                    self.df.iloc[-1]['High'] = price
                if price < self.df.iloc[-1]['High']:
                    self.df.iloc[-1]['Low'] = price

            self.timeout.emit(self.df)
            time.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.df = None
        self.plot = None

        # thread
        self.w = Worker()
        self.w.timeout.connect(self.update_data)
        self.w.start()

        # timer 
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.update)

        view = QGraphicsView()
        grid_layout = QGridLayout(view)
        self.setCentralWidget(view)
        self.resize(1200, 600)

        self.ax = fplt.create_plot(init_zoom_periods=100)    # pygtgraph.graphicsItems.PlotItem
        #axo = ax.overlay()                              # pygtgraph.graphicsItems.PlotItem
        self.axs = [self.ax]                                 # finplot requres this property
        grid_layout.addWidget(self.ax.vb.win, 0, 0)          # ax.vb     (finplot.FinViewBox)
        
    def update(self):
        now = datetime.datetime.now()
        self.statusBar().showMessage(str(now))

        if self.df is not None:
            if self.plot is None:
                self.plot = fplt.candlestick_ochl(self.df[['Open', 'Close', 'High', 'Low']])
                fplt.show(qt_exec=False)
            else:
                self.plot.update_data(self.df[['Open', 'Close', 'High', 'Low']])
 
    @pyqtSlot(pd.DataFrame)
    def update_data(self, df):
        self.df = df


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()