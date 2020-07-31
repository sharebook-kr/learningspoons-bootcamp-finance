import sys
from PyQt5.QtWidgets import *
import datetime

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)

        self.list_widget = QListWidget(self)
        self.list_widget.resize(250, 280)
        self.list_widget.move(10, 10)

        self.btn1 = QPushButton("추가", self)
        self.btn1.move(270, 10)
        self.btn1.clicked.connect(self.btn1_clicked)

        self.btn2 = QPushButton("초기화", self)
        self.btn2.move(270, 50)
        self.btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        now = datetime.datetime.now()
        self.list_widget.addItem(str(now))

    def btn2_clicked(self):
        self.list_widget.clear()

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()