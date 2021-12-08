from pyupbit import WebSocketManager
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Worker(QThread):
    recv = pyqtSignal(dict)

    def run(self):
        # create websocket for Upbit 
        self.wm = WebSocketManager("ticker", ["KRW-BTC"])
        while True:
            data = self.wm.get()
            self.recv.emit(data)

    def stop(self):
        self.wm.terminate()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("BTC", self)
        label.move(20, 20)

        self.price = QLabel("", self)
        self.price.move(80, 20)
        self.price.resize(100, 20)

        self.th = Worker()
        self.th.recv.connect(self.receive_msg)
        self.th.start()


    @pyqtSlot(dict)
    def receive_msg(self, data):
        close_price = data.get("trade_price")
        self.price.setText(str(close_price))

    def closeEvent(self, e):
        self.th.stop()
        return super().closeEvent(e)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   mywindow = MyWindow()
   mywindow.show()
   app.exec_()