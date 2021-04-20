import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import pyupbit


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window size
        self.setMinimumSize(600, 400)

        df = pyupbit.get_ohlcv("KRW-BTC")

        # data
        series = QLineSeries()
        for index in df.index:
            close = df.loc[index, 'close']
            dt = index.timestamp() * 1000       # msecs
            series.append(dt, close)

        # chart object
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)         # data feeding

        # axis
        axis_x = QDateTimeAxis()
        axis_x.setFormat("yyyy-MM-dd")
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