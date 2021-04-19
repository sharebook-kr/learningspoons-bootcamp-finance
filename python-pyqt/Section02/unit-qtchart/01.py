import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChart, QChartView, QLineSeries 
from PyQt5.QtGui import QPainter


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window size
        self.setMinimumSize(300, 200)

        # data
        series = QLineSeries()
        series.append(0, 0)
        series.append(1, 1)
        series.append(2, 2)

        # chart object
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)         # data feeding
        
        # displaying chart
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chart_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()