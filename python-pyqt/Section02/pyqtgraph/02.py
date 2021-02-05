import sys 
from PyQt5.QtWidgets import *
import pyqtgraph as pg 
import numpy as np


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        w = pg.PlotWidget(title="Basic Plot w/ symbol") 
        w.showGrid(x=True, y=True) 
        w.plot([1, 2, 3, 4], [1, 2, 3, 4], symbol='o')
        self.setCentralWidget(w)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()