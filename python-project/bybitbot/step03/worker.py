from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pybit import HTTP
import time

class Worker(QThread):
    last_price = pyqtSignal(list)

    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol 
        self.session = HTTP("https://api.bybit.com")

    def run(self):
        while True:
            info = self.session.latest_information_for_symbol(
                symbol=self.symbol
            )
            last_price = info['result'][0]['last_price']

            self.last_price.emit([self.symbol, last_price])
            time.sleep(1)
            