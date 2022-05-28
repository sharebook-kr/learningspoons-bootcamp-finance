import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
import pyupbit

class UpbitWS(QThread):
    poped = pyqtSignal(dict)

    def run(self):
        self.wm = pyupbit.WebSocketManager(type="ticker", codes=["KRW-BTC"])
        while True:
            data = self.wm.get()
            self.poped.emit(data)

    def terminate(self) -> None:
        self.wm.terminate()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w = pg.PlotWidget(axisItems= {'bottom': pg.DateAxisItem()})
        self.setCentralWidget(self.w)

        # thread
        self.wsc_upbit = UpbitWS()
        self.wsc_upbit.poped.connect(self.pop_upbit)
        self.wsc_upbit.start()

        self.xdata = []
        self.ydata = []

    @pyqtSlot(dict)
    def pop_upbit(self, data):
        close_price = data.get('trade_price')
        time_stamp = data.get('trade_timestamp')
        self.xdata.append(int(time_stamp/1000))
        self.ydata.append(close_price)
        self.w.plot(self.xdata, self.ydata)

    def closeEvent(self, event):
        self.wsc_upbit.terminate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()