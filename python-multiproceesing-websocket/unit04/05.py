import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import pyupbit


class Worker(QThread):
    mysignal = pyqtSignal(float)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            cur_price = pyupbit.get_current_price("KRW-BTC")
            self.mysignal.emit(cur_price)
            time.sleep(0.1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.mysignal.connect(self.myslot)
        self.worker.start()

    @pyqtSlot(float)
    def myslot(self, price):
        msg = f"BTC {price}"
        self.statusBar().showMessage(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()