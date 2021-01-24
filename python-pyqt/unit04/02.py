import sys 
from PyQt5.QtWidgets import *

def test():
    print("button clicked")

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton(text="버튼", parent=self)
        button.move(10, 10)
        button.clicked.connect(test)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()