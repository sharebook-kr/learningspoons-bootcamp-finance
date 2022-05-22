import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import threading


class Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            print("Worker thread", threading.current_thread().getName())
            self.sleep(2)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.start()
        print("MyWindow.__init__", threading.current_thread().getName())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()