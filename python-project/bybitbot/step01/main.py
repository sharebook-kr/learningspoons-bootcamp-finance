import datetime
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("ByBit Bot v1.0")
        self.setGeometry(100, 100, 1030, 300)

        labels = ["코인", "현재가", "상승장/하락장", "상승목표가", "하락목표가", "상태", "상승W", "상승K", "하락W", "하락K"]
        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(len(labels))
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(labels)

        self.text = QPlainTextEdit()

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.table)
        layout.addWidget(self.text)
        self.setCentralWidget(widget)

        # Timer
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.show_time)

    def show_time(self):
        now = datetime.datetime.now()
        self.statusBar().showMessage(str(now))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()