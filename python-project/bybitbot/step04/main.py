import datetime
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from worker import * 
from backtest import *
from binance.client import Client
from PyQt5.QtCore import Qt
import pprint


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("ByBit Bot v1.0 (양방향 변동성 돌파 전략)")
        self.setGeometry(100, 100, 930, 500)
        self.connect()

        self.worker = []
        self.backtest = []
        self.symbols = ['BTCUSDT', 'ETHUSDT', "XRPUSDT"]
        self.price_scales = {k:0 for k in self.symbols}
        self.labels = ["코인", "현재가", "상승목표가", "하락목표가", "상승W", "상승K", "하락W", "하락K", "보유상태"]

        self.label = QLabel("잔고")
        self.line_edit = QLineEdit(" ")
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.line_edit)
        hbox.addStretch(2)

        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(len(self.labels))
        self.table.setRowCount(len(self.symbols))
        self.table.setHorizontalHeaderLabels(self.labels)

        self.text = QPlainTextEdit()

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addLayout(hbox)
        layout.addWidget(self.table)
        layout.addWidget(self.text)
        self.setCentralWidget(widget)

        # Timer
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_ui)

        self.data = { symbol:{k:0 for k in self.labels} for symbol in self.symbols}
        self.create_threads()

    def connect(self):
        with open("../../../bybit.key") as f:
            lines = f.readlines()
            api_key = lines[0].strip()
            api_secret = lines[1].strip()

        self.session = HTTP(
            endpoint="https://api.bybit.com", 
            api_key=api_key, 
            api_secret=api_secret,
            spot=False
        )

        symbols = self.session.query_symbol()
        result = symbols['result']
        for symbol in result:
            name = symbol['name']
            price_scale = symbol["price_scale"]
            if name in self.scales.keys():
                self.price_scales[name] = price_scale

    def fetch_balance(self):
        balances = self.session.get_wallet_balance()
        usdt = balances['result']['USDT']['wallet_balance']
        self.line_edit.setText(str(usdt))

    def create_threads(self):
        for symbol in self.symbols:
            w = Worker(symbol)
            w.last_price.connect(self.update_last_price)
            w.start()
            self.worker.append(w)

            b = BackTest(symbol)
            b.params.connect(self.update_params)
            b.start()
            self.backtest.append(b)

    def update_ui(self):
        now = datetime.datetime.now()
        self.statusBar().showMessage(str(now))
        self.update_table_widget()
        self.fetch_balance()

    def update_table_widget(self):
        for r, symbol in enumerate(self.symbols):
            for c, lable in enumerate(self.labels):
                data = self.data[symbol][lable]

                if lable in ["상승목표가", "하락목표가"]:
                    data = "{:.3f}".format(data) 

                item = QTableWidgetItem(str(data))
                if c == 0:
                    item.setTextAlignment(Qt.AlignCenter)
                else:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                self.table.setItem(r, c, item)

    @pyqtSlot(list)
    def update_last_price(self, info):
        symbol, last = info 
        self.data[symbol]['코인'] = symbol
        self.data[symbol]['현재가'] = last

    @pyqtSlot(list)
    def update_params(self, params):
        symbol, up_target, up_window, up_k, down_target, down_window, down_k = params 

        self.data[symbol]['상승목표가'] = up_target
        self.data[symbol]['상승W'] = up_window 
        self.data[symbol]['상승K'] = "{:.2f}".format(up_k) 

        self.data[symbol]['하락목표가'] = down_target
        self.data[symbol]['하락W'] = down_window 
        self.data[symbol]['하락K'] = "{:.2f}".format(down_k) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()