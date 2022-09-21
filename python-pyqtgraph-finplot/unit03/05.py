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

        #df = pyupbit.get_ohlcv("KRW-BTC", interval='minute1')
        df = pyupbit.get_ohlcv("KRW-BTC", interval='day')
        x = [x.to_pydatetime().timestamp() for x in df.index]
        #x = [x.timestamp() for x in df.index]
        y = df['close']
        w.plot(x=x, y=y, pen=pg.mkPen(color='#2196F3', width=4))

        max_idx = df['close'].argmax()
        min_idx = df['close'].argmin()
        max_xpos = df.index[max_idx].to_pydatetime().timestamp()
        min_xpos = df.index[min_idx].to_pydatetime().timestamp()

        max_arrow = pg.ArrowItem(angle=-180, tipAngle=60, headLen=10, pen=None, brush='r')
        max_arrow.setPos(max_xpos, df['close'].iloc[max_idx])
        min_arrow = pg.ArrowItem(angle=-180, tipAngle=60, headLen=10, pen=None, brush='b')
        min_arrow.setPos(min_xpos, df['close'].iloc[min_idx])

        w.addItem(max_arrow)
        w.addItem(min_arrow)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()