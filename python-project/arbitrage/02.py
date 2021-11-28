from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit
import sys

class UpbitWS(QThread):
    poped = pyqtSignal(dict)

    def run(self):
        wm = pyupbit.WebSocketManager(type="orderbook", codes=["KRW-BTC"])
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

    @pyqtSlot(dict)
    def pop_upbit(self, data):
        orderbook = data["orderbook_units"][0]
        ask_price = orderbook["ask_price"]
        ask_size  = orderbook["ask_size"]
        bid_price = orderbook["bid_price"]
        bid_size  = orderbook["bid_size"]
        
        self.table.setItem(0, 0, QTableWidgetItem("Upibt"))
        self.table.setItem(0, 1, QTableWidgetItem(str(ask_price)))
        self.table.setItem(0, 2, QTableWidgetItem(str(ask_size)))
        self.table.setItem(0, 3, QTableWidgetItem(str(bid_price)))
        self.table.setItem(0, 4, QTableWidgetItem(str(bid_size)))


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