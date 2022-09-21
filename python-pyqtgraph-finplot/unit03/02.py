import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import pyupbit

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        w = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
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