# AxisItem displays dates from the unix timestamps.
import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import FinanceDataReader as fdr


class MyDateAxisItem(pg.DateAxisItem):
    def __init__(self, orientation, *args, **kwargs):
        super().__init__(orientation=orientation, *args, **kwargs)

    def tickStrings(self, values, scale, spacing):
        print(values, scale, spacing)
        return super().tickStrings(values, scale, spacing)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # layout
        w = pg.PlotWidget(axisItems={'bottom': MyDateAxisItem(orientation='bottom')})
        self.setCentralWidget(w)

        # data
        df = fdr.DataReader("005930")

        # style
        w.setBackground('w')
        w.setTitle("Title")
        w.setLabel("left", "y-axis")
        w.setLabel("bottom", "x-axis")
        w.addLegend()
        w.showGrid(x=True, y=True)

        # plot 
        unix_ts = [x.timestamp() for x in df.index]
        w.plot(x=unix_ts, y=df['Close'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()