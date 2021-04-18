import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit 


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        timer = QTimer(self)
        timer.start(1000)           # 1 sec
        timer.timeout.connect(self.display_price)

    def display_price(self):
        cur_price = pyupbit.get_current_price("KRW-BTC")
        self.statusBar().showMessage("BTC: " + str(cur_price))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()