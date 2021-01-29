import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        label1 = QLabel(text="고객 ID", parent=self)
        label1.resize(150, 30)
        label1.move(10, 10)

        label2 = QLabel(text="ID 비밀번호", parent=self)
        label2.resize(150, 30)
        label2.move(10, 50)

        label3 = QLabel(text="인증비밀번호", parent=self)
        label3.resize(150, 30)
        label3.move(10, 90)

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()