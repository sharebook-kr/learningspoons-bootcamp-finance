# plot when signal is emitted
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
import pyupbit
from datetime import datetime

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

        self.w = pg.PlotWidget(
            axisItems= {'bottom': pg.DateAxisItem()}
        )
        self.setCentralWidget(self.w)

        # thread
        self.wsc_upbit = UpbitWS()
        self.wsc_upbit.poped.connect(self.pop_upbit)
        self.wsc_upbit.start()

        self.xdata = []
        self.ydata = []
        self.time_stamp = int(datetime.now().timestamp())
        self.close_price = 0

    @pyqtSlot(dict)
    def pop_upbit(self, data):
        self.time_stamp = int(data.get('trade_timestamp') / 1000)
        self.close_price = data.get('trade_price')
        #print(self.time_stamp, self.close_price)

        if self.time_stamp not in self.xdata:
            # append
            self.xdata.append(self.time_stamp)
            self.ydata.append(self.close_price)
        else:
            # update
            index = self.xdata.index(self.time_stamp)
            self.ydata[index] = self.close_price

        # clear and plot
        self.w.setXRange(self.time_stamp-60, self.time_stamp+1, padding=0)
        self.w.clear()
        self.w.plot(self.xdata, self.ydata)

        # delete data
        try:
            index = self.xdata.index(self.time_stamp-60) + 1
            self.xdata = self.xdata[index: ]
            self.ydata = self.ydata[index: ]
        except ValueError:
            pass


    def closeEvent(self, event):
        self.wsc_upbit.terminate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()