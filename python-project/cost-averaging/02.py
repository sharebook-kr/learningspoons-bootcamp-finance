import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import * 
import pyupbit 

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Cost Averaging Upbit (Bitcoin) v1.0")
        self.create_table_widget()

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.table_widget)
        self.setCentralWidget(widget)

    def create_table_widget(self):
        # table widget
        self.table_widget = QTableWidget()
        labels = ['한글명', '현재가', '평단가']
        self.table_widget.setColumnCount(len(labels))
        self.table_widget.setRowCount(1)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setHorizontalHeaderLabels(labels)
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()