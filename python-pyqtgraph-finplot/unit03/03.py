import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import pyupbit
from math import ceil, log10


class YAxisItem(pg.AxisItem):
    def __init__(self, orientation='left', **kwargs):
        super().__init__(orientation, **kwargs)

    def tickStrings(self, values, scale, spacing):
        if self.logMode:
            return self.logTickStrings(values, scale, spacing)

        places = max(0, ceil(-log10(spacing*scale)))
        strings = []
        for v in values:
            vs = v * scale
            vstr = ("%%0.%df" % places) % vs
            strings.append(vstr)
        return strings


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        w = pg.PlotWidget(axisItems= {
            'left': YAxisItem(),
            'bottom': pg.DateAxisItem()
            }
        )
        self.setCentralWidget(w)

        df = pyupbit.get_ohlcv("KRW-BTC")
        x = [x.timestamp() for x in df.index]
        y = df['close']

        w.setBackground('w')
        pen = pg.mkPen('k', width=2)
        w.plot(x=x, y=y, pen=pen)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()