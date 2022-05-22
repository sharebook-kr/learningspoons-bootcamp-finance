import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit

ROW_INDEX_LOOKUP = {
    "KRW-BTC": 0,
    "KRW-ETH": 1,
    "KRW-XRP": 2
}

class Worker(QThread):
    poped = pyqtSignal(dict)

    def run(self):
        self.wm = pyupbit.WebSocketManager(
            type="ticker",
            codes=["KRW-XRP", "KRW-BTC", "KRW-ETH"]
        )

        while True:
            data = self.wm.get()
            self.poped.emit(data)

    def terminate(self):
        return self.wm.terminate()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.start()
        self.worker.poped.connect(self.receive_data)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setRowCount(3)
        self.table.setHorizontalHeaderLabels(["암호화폐", "현재가"])

        # layout
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.table)
        self.setCentralWidget(widget)

    @pyqtSlot(dict)
    def receive_data(self, data):
        code = data["code"]
        close_price = data["trade_price"]
        row = ROW_INDEX_LOOKUP[code]
        self.table.setItem(row, 0, QTableWidgetItem(code))
        self.table.setItem(row, 1, QTableWidgetItem(str(close_price)))

    def closeEvent(self, event):
        self.worker.terminate()
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()