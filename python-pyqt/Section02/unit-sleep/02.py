import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.btn = QPushButton("Sleep", self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.sleep)

    def timeout(self):
        print("timer is working")

    def sleep(self):
        print("sleep start")
        #time.sleep(5)
        QTest.qWait(5000)
        print("sleep end")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()