# candlestick with minute OHLC
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtChart import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtCore import * 
import pyupbit
import time
from pandas import Series


class Worker(QThread):
    price = pyqtSignal(float)
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            cur_price = pyupbit.get_current_price("KRW-BTC")
            self.price.emit(cur_price)
            time.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # thread 
        self.worker = Worker()
        self.worker.price.connect(self.get_price)
        self.worker.start()

        self.minute_cur = QDateTime.currentDateTime()   # current
        self.minute_pre = self.minute_cur.addSecs(-60)  # 1 minute ago
        self.ticks = Series(dtype='float64') 

        # window size
        self.setMinimumSize(800, 400)
        df = pyupbit.get_ohlcv("KRW-BTC", interval='minute1', count=80)

        # data
        self.series = QCandlestickSeries()
        self.series.setIncreasingColor(Qt.red)
        self.series.setDecreasingColor(Qt.blue)

        # initial OHLC feeding 
        for index in df.index:
            open = df.loc[index, 'open']
            high = df.loc[index, 'high']
            low = df.loc[index, 'low']
            close = df.loc[index, 'close']

            # time conversion
            format = "%Y-%m-%d %H:%M:%S"
            str_time = index.strftime(format)
            dt = QDateTime.fromString(str_time, "yyyy-MM-dd hh:mm:ss")
            ts = dt.toMSecsSinceEpoch()
            #ts = index.timestamp() * 1000
            #print(ts)

            elem = QCandlestickSet(open, high, low, close, ts)
            self.series.append(elem)

        # chart object
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(self.series)         # data feeding

        # axis
        axis_x = QDateTimeAxis()
        axis_x.setFormat("hh:mm:ss")
        chart.addAxis(axis_x, Qt.AlignBottom)
        self.series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setLabelFormat("%i")
        chart.addAxis(axis_y, Qt.AlignLeft)
        self.series.attachAxis(axis_y)

        # margin
        chart.layout().setContentsMargins(0, 0, 0, 0)

        # displaying chart
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chart_view)


    @pyqtSlot(float)
    def get_price(self, cur_price):
        # append current price
        dt = QDateTime.currentDateTime()
        self.statusBar().showMessage(dt.toString())
        self.ticks[dt] = cur_price

        # check whether minute changed
        #if dt.time().minute() != self.minute_cur.time().minute():


        ts = dt.toMSecsSinceEpoch()
        print(ts, cur_price)

        sets = self.series.sets()
        last_set = sets[-1]                  

        open = last_set.open()
        high = last_set.high()
        low = last_set.low()
        close = last_set.close()
        ts1 = last_set.timestamp()
        self.series.remove(last_set)        # remove last set

        new_set = QCandlestickSet(open, high, low, cur_price, ts1)
        self.series.append(new_set)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()