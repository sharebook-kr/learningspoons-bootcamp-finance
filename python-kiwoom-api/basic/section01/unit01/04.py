import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("매수", self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()

