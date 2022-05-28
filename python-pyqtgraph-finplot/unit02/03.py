import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        w = pg.PlotWidget()
        x = [1, 2, 3, 4]
        y = [1, 2, 3, 4]

        # style
        w.setBackground('w')
        w.setTitle("Title")
        w.setLabel("left", "y-axis")
        w.setLabel("bottom", "x-axis")
        w.showGrid(x=True, y=True)
        w.addLegend()

        w.plot(x, y, pen=pg.mkPen(width=4, color='r'), name="plot-1")
        self.setCentralWidget(w)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()