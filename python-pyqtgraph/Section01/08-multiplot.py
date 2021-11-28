import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # layout
        w = pg.PlotWidget()
        self.setCentralWidget(w)

        # data
        x1 = [1, 2, 3, 4]
        y1 = [1, 2, 3, 4]
        x2 = [1, 2, 3, 4]
        y2 = [1, 4, 9, 16]

        # style
        w.setBackground('w')
        w.setTitle("Title")
        w.setLabel("left", "y-axis")
        w.setLabel("bottom", "x-axis")
        w.addLegend()
        w.showGrid(x=True, y=True)

        # plot 
        w.plot(x=x1, y=y1, pen=pg.mkPen(width=2, color='r'), name="plot1")
        w.plot(x=x2, y=y2, pen=pg.mkPen(width=2, color='b'), name="plot2")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()