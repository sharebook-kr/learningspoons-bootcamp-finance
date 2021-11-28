from pybithumb import WebSocketManager
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import time
import pprint
import pybithumb


class Worker(QThread):
    recv = pyqtSignal(dict)
    def run(self):
        # create websocket for Bithumb
        #wm = WebSocketManager("ticker", ["BTC_KRW"])
        wm = WebSocketManager("orderbookdepth", ["BTC_KRW"])
        while True:
            data = wm.get()
            self.recv.emit(data)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("BTC", self)
        label.move(20, 20)

        self.price = QLabel("-", self)
        self.price.move(80, 20)
        self.price.resize(100, 20)

        self.th = Worker()
        self.th.recv.connect(self.receive_msg)
        self.th.start()

    @pyqtSlot(dict)
    def receive_msg(self, data):
        #print(data.keys())
        datetime = data['content']['datetime']
        orderbooks = data['content']['list']

        for orderbook in orderbooks:
            order_type = orderbook['orderType']
            price = orderbook['price']
            quantitiy = orderbook['quantity']

            if (69500000 < float(price) < 69600000):
                print(price, quantitiy)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   mywindow = MyWindow()
   mywindow.show()
   app.exec_()