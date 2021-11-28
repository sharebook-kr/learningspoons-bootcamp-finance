import websockets
import asyncio 
import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import multiprocessing as mp
import datetime


async def upbit_ws_client(q):
    uri = "wss://api.upbit.com/websocket/v1"

    async with websockets.connect(uri, ping_interval=60) as websocket:
        subscribe_fmt = [
            {"ticket": "test"},
            {"type": "ticker", "codes": ["KRW-BTC"], "isOnlyRealtime": True},
            {"format": "DEFAULT"}
        ]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            rdata = await websocket.recv()
            data = json.loads(rdata)
            q.put(data)


def producer(q):
    asyncio.run(upbit_ws_client(q))


class Consumer(QThread):
    poped = pyqtSignal(dict)

    def __init__(self, q):
        super().__init__() 
        self.q = q 

    def run(self):
        while True:
            data = q.get() 
            self.poped.emit(data)


class MyWindow(QMainWindow):
    def __init__(self, q):
        super().__init__()
        self.consumer = Consumer(q)
        self.consumer.poped.connect(self.receive_real)
        self.consumer.start() 

    @pyqtSlot(dict)
    def receive_real(self, data):
        price = data['trade_price']
        self.statusBar().showMessage(str(price))


if __name__ == "__main__":
    # Producer
    q = mp.Queue()
    p = mp.Process(name="Producer", target=producer, args=(q,), daemon=True)
    p.start()

    # MainProcess
    app = QApplication(sys.argv)
    window = MyWindow(q)
    window.show()
    app.exec_()

