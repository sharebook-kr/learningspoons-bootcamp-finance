from PyQt5.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle("Coin Arbitrage v0.1")
        self.create_table_widget()

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def create_table_widget(self):
        self.table = QTableWidget()
        columns = ["exchange", "ask", "ask volume", "bid", "bid volume", "price", "gap"]
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(len(columns))
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(columns)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()