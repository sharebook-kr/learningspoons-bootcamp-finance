import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Worker(QThread):
    mysignal = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        num = 0
        while True:
            self.mysignal.emit(num)
            num += 1
            self.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.start()
        self.worker.mysignal.connect(self.receive_data)

    @pyqtSlot(int)
    def receive_data(self, data):
        print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()