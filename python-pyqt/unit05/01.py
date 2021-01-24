import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        btn1 = QPushButton("Trading Start", self)
        btn1.resize(150, 30)
        btn1.move(10, 10)

        btn2 = QPushButton("Trading Stop", self)
        btn2.resize(150, 30)
        btn2.move(10, 50)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()