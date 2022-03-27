import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import * 
import pyupbit 
import math
import datetime


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("무한매수 프로그램 v1.0 (UpBit)")
        self.create_table_widget()

        # timer 
        self.timer_price = QTimer(self)
        self.timer_price.start(1000)
        self.timer_price.timeout.connect(self.update_price)

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.table_widget)
        self.setCentralWidget(widget)

    def create_table_widget(self):
        krw_tickers = pyupbit.get_tickers(fiat="KRW")

        self.table_widget = QTableWidget()
        self.table_widget.setSortingEnabled(True)
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(len(krw_tickers))
        self.table_widget.verticalHeader().setVisible(False)

        labels = ['ticker', 'price', 'RSI']
        self.table_widget.setHorizontalHeaderLabels(labels)
        self.update_price()

    def query_price(self, tickers):
        hundred = math.ceil(len(tickers) / 100)        # 110 -> 2

        result = {}
        for i in range(hundred):
            tickers100 = tickers[100*i:100*i+100]
            cur_price = pyupbit.get_current_price(tickers100)
            result.update(cur_price)

        return result

    def update_price(self):
        now = datetime.datetime.now()
        self.statusBar().showMessage(str(now))

        krw_tickers = pyupbit.get_tickers(fiat="KRW")
        self.table_widget.setRowCount(len(krw_tickers))
        price = self.query_price(krw_tickers)

        row = 0
        for ticker, cur_price in price.items():
            item = QTableWidgetItem(ticker)
            item.setTextAlignment(int(Qt.AlignCenter|Qt.AlignVCenter))
            self.table_widget.setItem(row, 0, item) 

            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, int(cur_price))
            item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
            self.table_widget.setItem(row, 1, item) 
            row += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()