import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 300, 320)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 310)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        
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

            widget = QWidget()
            layout = QVBoxLayout(widget)
            pbar = QProgressBar()
            pbar.setFixedHeight(20)
            pbar.setInvertedAppearance(True)  
            pbar.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            pbar.setStyleSheet("""
                QProgressBar {background-color : rgba(0, 0, 0, 0%);border : 1}
                QProgressBar::Chunk {background-color : rgba(0, 0, 255, 20%);border : 1}
            """)
            layout.addWidget(pbar)
            layout.setAlignment(Qt.AlignVCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(layout)
            self.tableWidget.setCellWidget(i, 0, widget)

            # set data 
            pbar.setRange(0, 10000)
            pbar.setFormat(str(quantity))
            pbar.setValue(quantity)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()