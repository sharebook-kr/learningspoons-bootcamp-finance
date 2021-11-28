import sys
from PyQt5.QtCore import QThread 
from PyQt5.QtWidgets import *
import time
import threading


class Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        tname = threading.currentThread().getName()
        while True:
            print("run", tname)
            time.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        tname = threading.currentThread().getName()
        print("__init__", tname)

        # create thread 
        self.worker = Worker()
        self.worker.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()