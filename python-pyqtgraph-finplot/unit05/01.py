import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import numpy as np


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        w = pg.PlotWidget(background='w')
        self.setCentralWidget(w)

        x = np.arange(20)
        y = np.random.randint(low=0, high=100, size=20)
        bar = pg.BarGraphItem(x=x, height=y, width=0.3, pen=None, brush='b')
        w.addItem(bar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()