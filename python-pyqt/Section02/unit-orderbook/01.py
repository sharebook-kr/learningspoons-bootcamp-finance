import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 300, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(9)
        
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)

        #self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnWidth(0, int(self.tableWidget.width() * 0.4))
        self.tableWidget.setColumnWidth(1, int(self.tableWidget.width() * 0.2))
        self.tableWidget.setColumnWidth(2, int(self.tableWidget.width() * 0.4)) 

        # price 
        for i in range(10):
            price = 4000 - i * 10
            item = QTableWidgetItem(format(price, ","))
            item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
            self.tableWidget.setItem(i, 1, item)

        # quantity
        for i in range(10):
            quantity = random.randint(1, 5000) 
            item = QTableWidgetItem(format(quantity, ","))
            item.setTextAlignment(int(Qt.AlignRight|Qt.AlignVCenter))
            self.tableWidget.setItem(i, 0, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()