import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import * 
import pyupbit 

f = open("../../upbit.key")
lines = f.readlines()
f.close()

access = lines[0].strip()
secret = lines[1].strip()
upbit = pyupbit.Upbit(access, secret)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle("Cost Averaging Upbit (Bitcoin) v1.0")
        self.create_table_widget()

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.table_widget)
        self.setCentralWidget(widget)

        # timer 
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_price)

    def update_price(self):
        btc_price = pyupbit.get_current_price("KRW-BTC")        
        balances = upbit.get_balances()

        # 비트코인 평단가 
        krw_btc_balance = None
        for balance in balances:
            if balance['currency'] == "BTC" and balance['unit_currency'] == "KRW":
                krw_btc_balance = balance
                break

        try:
            btc_avg_buy_price = int(krw_btc_balance['avg_buy_price'])
        except:
            btc_avg_buy_price = 0

        item = QTableWidgetItem(format(btc_price, ","))
        item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
        self.table_widget.setItem(0, 1, item) 

        item = QTableWidgetItem(format(btc_avg_buy_price, ","))
        item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
        self.table_widget.setItem(0, 2, item) 

        # 평가손익 
        percent = (btc_price - btc_avg_buy_price) / btc_price * 100
        item = QTableWidgetItem(f"{percent:.2f} %")
        item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
        self.table_widget.setItem(0, 3, item) 

    def create_table_widget(self):
        # table widget
        self.table_widget = QTableWidget()
        labels = ['보유코인', '현재가', '매수평균가', '평가손익']
        self.table_widget.setColumnCount(len(labels))
        self.table_widget.setRowCount(1)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setHorizontalHeaderLabels(labels)

        item = QTableWidgetItem("비트코인")
        item.setTextAlignment(int(Qt.AlignCenter|Qt.AlignVCenter))
        self.table_widget.setItem(0, 0, item) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()