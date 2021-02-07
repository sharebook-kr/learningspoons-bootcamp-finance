import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 200, 400, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(380, 270)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)

        labels = ["종목명", "종목코드"]
        self.tableWidget.setHorizontalHeaderLabels(labels)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("삼성전자"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("005930"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("SK하이닉스"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("000660"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("NAVER"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("035420"))

        self.tableWidget.currentCellChanged.connect(self.slot)

    def slot(self, curr_row, curr_col, prev_row, prev_col):
        print(curr_row, curr_col)
        item = self.tableWidget.item(curr_row, curr_col)
        text = item.text()
        self.statusBar().showMessage(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()