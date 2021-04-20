import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChart, QChartView, QLineSeries 
from PyQt5.QtGui import QPainter


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window size
        self.setMinimumSize(600, 400)

        # data
        raw_data = [
            (0, 6),
            (2, 4),
            (3, 8),
            (7, 4),
            (10, 5),
            (11, 1),
            (13, 3),
            (17, 6),
            (18, 3),
            (20, 2)
        ]

        series = QLineSeries()
        for d in raw_data:
            series.append(*d)

        # chart object
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)         # data feeding
        chart.createDefaultAxes()
        
        # displaying chart
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chart_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()