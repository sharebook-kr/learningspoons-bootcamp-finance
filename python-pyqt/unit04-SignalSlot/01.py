import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton(text="버튼", parent=self)
        button.move(10, 10)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()