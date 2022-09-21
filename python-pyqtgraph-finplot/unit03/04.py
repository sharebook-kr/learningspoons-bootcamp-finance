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
            },
            background='w'
        )
        self.setCentralWidget(w)

        df = pyupbit.get_ohlcv("KRW-BTC", interval='minute1')
        x = [x.to_pydatetime().timestamp() for x in df.index]
        y = df['close']
        y2 = df['close'].rolling(window=9).mean()

        w.addLegend()
        w.plot(x=x, y=y, pen=pg.mkPen(color='#2196F3', width=4), name="minute1")
        w.plot(x=x, y=y2, pen=pg.mkPen(color='r', width=2), name='MA 9')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()