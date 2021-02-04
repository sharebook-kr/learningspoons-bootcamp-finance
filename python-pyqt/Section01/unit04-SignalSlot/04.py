import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton(text="종료", parent=self)
        button.move(10, 10)
        button.clicked.connect(QApplication.instance().quit)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()