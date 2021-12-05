from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit
import pykorbit
import sys
import pprint
import asyncio
import datetime
import websockets
import json
import multiprocessing as mp


class KorbitWS(QThread):
    poped = pyqtSignal(dict)

    def run(self):
        wm = pykorbit.WebSocketManager(['orderbook:xrp_krw'])
        while True:
            data = wm.get()
            self.poped.emit(data)


class UpbitWS(QThread):
    poped = pyqtSignal(dict)

    def run(self):
        wm = pyupbit.WebSocketManager(type="orderbook", codes=["KRW-XRP"])
        while True:
            data = wm.get()
            self.poped.emit(data)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 650, 300)
        self.setWindowTitle("Coin Arbitrage v0.1")

        self.create_table_widget()
        self.create_ws_threads()

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def create_ws_threads(self):
        self.wsc_upbit = UpbitWS()
        self.wsc_upbit.poped.connect(self.pop_upbit)
        self.wsc_upbit.start()

        self.wsc_korbit = KorbitWS()
        self.wsc_korbit.poped.connect(self.pop_korbit)
        self.wsc_korbit.start()

    @pyqtSlot(dict)
    def pop_upbit(self, data):
        orderbook = data["orderbook_units"][0]
        ask_price = orderbook["ask_price"]
        ask_size  = orderbook["ask_size"]
        bid_price = orderbook["bid_price"]
        bid_size  = orderbook["bid_size"]
        
        self.table.setItem(0, 0, QTableWidgetItem("Upibt"))
        self.table.setItem(0, 1, QTableWidgetItem(str(int(ask_price))))
        self.table.setItem(0, 2, QTableWidgetItem(str(ask_size)))
        self.table.setItem(0, 3, QTableWidgetItem(str(int(bid_price))))
        self.table.setItem(0, 4, QTableWidgetItem(str(bid_size)))

    @pyqtSlot(dict)
    def pop_korbit(self, data):
        try:
            ask0 = data['data']['asks'][0] 
            bid0 = data['data']['bids'][0] 
            ask_price = ask0["price"]
            ask_size  = ask0["amount"]
            bid_price = bid0["price"]
            bid_size  = bid0["amount"]
                
            self.table.setItem(1, 0, QTableWidgetItem("Korbit"))
            self.table.setItem(1, 1, QTableWidgetItem(str(ask_price)))
            self.table.setItem(1, 2, QTableWidgetItem(str(ask_size)))
            self.table.setItem(1, 3, QTableWidgetItem(str(bid_price)))
            self.table.setItem(1, 4, QTableWidgetItem(str(bid_size)))
        except:
            pass

    def create_table_widget(self):
        self.table = QTableWidget()
        columns = ["exchange", "ask price", "ask size", "bid price", "bid size", "gap"]
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(len(columns))
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(columns)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()