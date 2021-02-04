import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        btn1 = QPushButton("Trading Start", self)
        btn1.resize(150, 30)
        btn1.move(10, 10)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        print("start !!")

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()