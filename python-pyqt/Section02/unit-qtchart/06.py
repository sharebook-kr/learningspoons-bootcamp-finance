import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QPointF, QDateTime
import pyupbit
import time
import datetime


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

        # window size
        self.setMinimumSize(600, 400)

        # data
        self.series = QLineSeries()

        # chart object
        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)         # data feeding

        # axis
        axis_x = QDateTimeAxis()
        axis_x.setFormat("hh:mm:ss")

        dt = QDateTime.currentDateTime()
        axis_x.setRange(dt, dt.addSecs(128))

        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self.series.attachAxis(axis_x)
        

        axis_y = QValueAxis()
        axis_y.setLabelFormat("%i")
        self.chart.addAxis(axis_y, Qt.AlignLeft)
        self.series.attachAxis(axis_y)

        # margin
        self.chart.layout().setContentsMargins(0, 0, 0, 0)

        # displaying chart
        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chart_view)

    @pyqtSlot(float)
    def get_price(self, cur_price):
        if len(self.series) == 128:
            self.series.remove(0)       # delete first data
        
        # append current price
        dt = QDateTime.currentDateTime()
        ts = dt.toMSecsSinceEpoch()
        self.series.append(ts, cur_price)
        print(ts, cur_price)

        # update asis
        data = self.series.pointsVector()
        first_ts = data[0].x()
        last_ts = data[-1].x()
        first_dt = QDateTime.fromMSecsSinceEpoch(first_ts)
        last_dt = QDateTime.fromMSecsSinceEpoch(last_ts)

        axis_x = self.chart.axisX()
        axis_x.setRange(first_dt, last_dt)

        axis_y = self.chart.axisY()
        axis_y.setRange(70000000, 71000000)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()