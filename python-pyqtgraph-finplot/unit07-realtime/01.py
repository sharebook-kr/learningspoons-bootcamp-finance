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

        # thread
        self.wsc_upbit = UpbitWS()
        self.wsc_upbit.poped.connect(self.pop_upbit)
        self.wsc_upbit.start()

    @pyqtSlot(dict)
    def pop_upbit(self, data):
        close_price = data.get('trade_price')
        time_stamp = int(data.get('trade_timestamp') / 1000)     # msec -> sec
        print(close_price, time_stamp)

    def closeEvent(self, event):
        self.wsc_upbit.terminate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()