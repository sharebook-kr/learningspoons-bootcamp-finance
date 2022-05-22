import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit


class Worker(QThread):
    poped = pyqtSignal(dict)

    def run(self):
        self.wm = pyupbit.WebSocketManager(
            type="ticker",
            codes=["KRW-XRP", "KRW-BTC", "KRW-ETH"]
        )

        while True:
            data = self.wm.get()
            self.poped.emit(data)

    def terminate(self):
        return self.wm.terminate()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.start()
        self.worker.poped.connect(self.receive_data)

    @pyqtSlot(dict)
    def receive_data(self, data):
        print(data)

    def closeEvent(self, event):
        self.worker.terminate()
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()