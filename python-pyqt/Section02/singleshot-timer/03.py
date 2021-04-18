import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import threading
import time


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.timeout)

    def timeout(self):
        name = threading.currentThread().getName()
        print(f"{name}")
        print("before sleep")
        time.sleep(5)
        print("after sleep")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()