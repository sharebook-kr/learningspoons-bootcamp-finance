from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit
import pybithumb
import sys
import pprint
import asyncio
import datetime
import websockets
import json
import multiprocessing as mp


async def korbit_ws_client(q):
    uri = "wss://ws.korbit.co.kr/v1/user/push"

    async with websockets.connect(uri) as websocket:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp() * 1000)

        subscribe_fmt = {
            "accessToken": None, 
            "timestamp": timestamp, 
            "event": "korbit:subscribe",
            "data": {
                "channels": ["orderbook:xrp_krw"]
            }
        }
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            rdata = await websocket.recv()
            data = json.loads(rdata)
            q.put(data)

def korbit(q):
    asyncio.run(korbit_ws_client(q))


class KorbitWS(QThread):
    poped = pyqtSignal(dict)

    def __init__(self, q):
        super().__init__()
        self.q = q 

    def run(self):
        while True:
            data = self.q.get() 
            self.poped.emit(data)


class UpbitWS(QThread):
    poped = pyqtSignal(dict)

    def run(self):
        wm = pyupbit.WebSocketManager(type="orderbook", codes=["KRW-XRP"])
        while True:
            data = wm.get()
            self.poped.emit(data)


class MyWindow(QWidget):
    def __init__(self, q):
        super().__init__()
        self.q = q
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

        self.wsc_korbit = KorbitWS(self.q)
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
        self.table.setItem(0, 1, QTableWidgetItem(str(ask_price)))
        self.table.setItem(0, 2, QTableWidgetItem(str(ask_size)))
        self.table.setItem(0, 3, QTableWidgetItem(str(bid_price)))
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
    q = mp.Queue()
    p = mp.Process(name="Korbit", target=korbit, args=(q,), daemon=True)
    p.start()

    app = QApplication(sys.argv)
    window = MyWindow(q)
    window.show()
    app.exec_()