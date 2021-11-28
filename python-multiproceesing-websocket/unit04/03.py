import sys
from PyQt5.QtCore import QThread 
from PyQt5.QtWidgets import *
import time
import threading
import pyupbit


class Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            cur_price = pyupbit.get_current_price("KRW-BTC")
            print(cur_price)
            time.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create thread 
        self.worker = Worker()
        self.worker.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()