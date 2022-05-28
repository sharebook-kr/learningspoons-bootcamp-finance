import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import numpy as np


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        w = pg.GraphicsLayoutWidget()
        self.setCentralWidget(w)

        p1 = w.addPlot(row=1, col=1, colspan=2)
        p2 = w.addPlot(row=2, col=1, colspan=2)
        p31 = w.addPlot(row=3, col=1)
        p32 = w.addPlot(row=3, col=2)

        p1.plot([1, 4, 2, 4, 3, 5])
        p1.setLabel(axis='bottom', text='x')
        p1.setLabel(axis='left', text='y')
        p1.setTitle("plot-1")
        p1.showGrid(x=True, y=True)

        p2.plot([1, 4, 2, 4, 3, 5])
        p31.plot([1, 4, 2, 4, 3, 5])
        p32.plot([1, 4, 2, 4, 3, 5])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()