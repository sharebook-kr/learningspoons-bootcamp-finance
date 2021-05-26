# candlestick with minute OHLC
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtChart import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtCore import * 
import pyupbit


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window size
        self.setMinimumSize(800, 400)
        df = pyupbit.get_ohlcv("KRW-BTC", interval='minute1', count=80)

        # data
        series = QCandlestickSeries()
        series.setIncreasingColor(Qt.red)
        series.setDecreasingColor(Qt.blue)

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
            series.append(elem)

        # chart object
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)         # data feeding

        # axis
        axis_x = QDateTimeAxis()
        axis_x.setFormat("hh:mm:ss")
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setLabelFormat("%i")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        # margin
        chart.layout().setContentsMargins(0, 0, 0, 0)


        # displaying chart
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chart_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()