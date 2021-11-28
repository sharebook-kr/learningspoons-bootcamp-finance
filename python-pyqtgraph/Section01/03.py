import sys 
from PyQt5.QtWidgets import *
import pyqtgraph as pg 
import numpy as np


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        w = pg.PlotWidget(title="Multiple Plotting") 
        w.showGrid(x=True, y=True) 
        w.addLegend()

        w.plot([1, 2, 3, 4], [1, 2, 3, 4], pen=(255, 0, 0), name="plot1")
        w.plot([1, 2, 3, 4], [10, 20, 30, 40], pen=(0, 0, 255), name="plot2")
        self.setCentralWidget(w)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()