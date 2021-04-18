import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import threading


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        timer = QTimer(self)
        timer.start(1000)
        timer.timeout.connect(self.timeout)

    def timeout(self):
        cur_thread = threading.currentThread()
        thread_name = cur_thread.getName()
        msg = f"name: {thread_name}"
        self.statusBar().showMessage(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()