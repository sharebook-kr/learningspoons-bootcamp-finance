import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit
import datetime

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Bitcoin: ", self)
        self.label.move(10, 10)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(80, 10)
        self.line_edit.resize(100, 30)

        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.handle_timer)

    def handle_timer(self):
        btc = pyupbit.get_current_price("KRW-BTC")
        self.line_edit.setText(str(btc))
        now = datetime.datetime.now()
        self.statusBar().showMessage(str(now))

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
