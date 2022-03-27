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

        # variables
        self.unit_seed = 0
        self.unit_max = 200
        self.unit_num = 200
        self.profit_ratio = 5
        self.initialize_unit_seed()

        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle("Cost Averaging Upbit (Bitcoin) v1.0")
        self.create_table_widget()

        widget = QWidget()
        layout = QVBoxLayout(widget)

        # top 
        layout_grid = QGridLayout()
        self.label1 = QLabel("총 보유자산")
        self.label2 = QLabel("유닛개수")
        self.label3 = QLabel("잔여 유닛개수")
        self.label4 = QLabel("하루 매수액")
        self.label5 = QLabel("매수시간")
        self.label6 = QLabel("익절률")

        self.lineedit_balance = QLineEdit()
        self.lineedit_balance.setEnabled(False)

        self.lineedit2 = QLineEdit()
        self.lineedit3 = QLineEdit()
        self.lineedit4 = QLineEdit()
        self.timeedit  = QTimeEdit()
        self.timeedit.setTime(QTime(9, 0, 0))
        self.timeedit.setDisplayFormat('hh:mm:ss')
        self.lineedit6 = QLineEdit()

        self.btn_unit_max = QPushButton("변경")
        self.btn_profit_ratio = QPushButton("변경")

        layout_grid.addWidget(self.label1, 0, 0)
        layout_grid.addWidget(self.label2, 1, 0)
        layout_grid.addWidget(self.label3, 2, 0)
        layout_grid.addWidget(self.label4, 3, 0)
        layout_grid.addWidget(self.label5, 4, 0)
        layout_grid.addWidget(self.label6, 5, 0)

        layout_grid.addWidget(self.lineedit_balance, 0, 1)
        layout_grid.addWidget(self.lineedit2, 1, 1)
        layout_grid.addWidget(self.lineedit3, 2, 1)
        layout_grid.addWidget(self.lineedit4, 3, 1)
        layout_grid.addWidget(self.timeedit , 4, 1)
        layout_grid.addWidget(self.lineedit6, 5, 1)

        layout_grid.addWidget(self.btn_unit_max, 1, 2)
        layout_grid.addWidget(self.btn_profit_ratio, 5, 2)

        layout_hbox = QHBoxLayout()
        self.btn_start = QPushButton("자동매수 시작")
        self.btn_stop = QPushButton("자동매수 중지")
        layout_hbox.addWidget(self.btn_start)
        layout_hbox.addWidget(self.btn_stop)
        layout_hbox.addStretch(2)

        self.plain_text = QPlainTextEdit()

        layout.addLayout(layout_grid)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.plain_text)
        layout.addLayout(layout_hbox)
        self.setCentralWidget(widget)

        # timer 
        self.timer = QTimer()
        self.timer.start(2000)
        self.timer.timeout.connect(self.update_price)

    def initialize_unit_seed(self):
        krw = upbit.get_balance_t("KRW")
        self.unit_seed = krw / self.unit_max

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

        # 총보유자산 
        # 원화 및 BTC만 고려함. 
        krw = upbit.get_balance_t("KRW")
        btc = upbit.get_balance_t("BTC") 
        total = krw + btc_price * btc 
        total = int(total)
        self.lineedit_balance.setText(format(total, ","))

        # 유닛개수
        self.lineedit2.setText(str(self.unit_max))
        # 잔여 유닛개수
        self.lineedit3.setText(str(self.unit_num))
        # 하루 매수액
        self.lineedit4.setText(f"{self.unit_seed:.1f}")
        # 익적률
        self.lineedit6.setText(str(self.profit_ratio))

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