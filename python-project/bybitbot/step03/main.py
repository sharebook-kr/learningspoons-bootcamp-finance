import datetime
import enum
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from worker import * 
from backtest import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("ByBit Bot v1.0 (양방향 변동성 돌파 전략)")
        self.setGeometry(100, 100, 1030, 300)

        self.symbols = ['BTCUSDT', 'ETHUSDT']
        self.labels = ["코인", "현재가", "상승장/하락장", "상승목표가", "하락목표가", "상태", "상승W", "상승K", "하락W", "하락K"]

        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(len(self.labels))
        self.table.setRowCount(len(self.symbols))
        self.table.setHorizontalHeaderLabels(self.labels)

        self.text = QPlainTextEdit()

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.table)
        layout.addWidget(self.text)
        self.setCentralWidget(widget)

        # Timer
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_ui)

        self.data = {
            self.symbols[0]: {k:0 for k in self.labels},
            self.symbols[1]: {k:0 for k in self.labels}
        }
        self.create_threads()

    def create_threads(self):
        self.worker1 = Worker(self.symbols[0])
        self.worker1.last_price.connect(self.update_last_price)
        self.worker1.start()

        self.worker2 = Worker(self.symbols[1])
        self.worker2.last_price.connect(self.update_last_price)
        self.worker2.start()

        self.back_test1 = BackTest(self.symbols[0])
        self.back_test1.params.connect(self.update_params)
        self.back_test1.start()

        self.back_test2 = BackTest(self.symbols[1])
        self.back_test2.params.connect(self.update_params)
        self.back_test2.start()

    def update_ui(self):
        now = datetime.datetime.now()
        self.statusBar().showMessage(str(now))
        self.update_table_widget()

    def update_table_widget(self):
        for r, symbol in enumerate(self.symbols):
            for c, lable in enumerate(self.labels):
                data = self.data[symbol][lable]
                item = QTableWidgetItem(str(data))
                self.table.setItem(r, c, item)

    @pyqtSlot(list)
    def update_last_price(self, info):
        symbol, last = info 
        self.data[symbol]['코인'] = symbol
        self.data[symbol]['현재가'] = last

    @pyqtSlot(list)
    def update_params(self, params):
        symbol, window, k = params 
        self.data[symbol]['상승W'] = window 
        self.data[symbol]['상승K'] = "{:.2f}".format(k) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()