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
        x = [1, 2, 3, 4]
        y = [1, 4, 9, 16]

        # Style
        w.setBackground('w')
        w.setTitle("Title")
        w.setLabel("left", "y-axis")
        w.setLabel("bottom", "x-axis")
        w.showGrid(x=True, y=True)
        w.addLegend()

        # plot
        w.plot(x, y, pen=(0, 0, 255), name="default plot")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()