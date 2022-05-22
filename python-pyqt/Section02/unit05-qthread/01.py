import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            print("Worker thread")
            self.sleep(2)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()