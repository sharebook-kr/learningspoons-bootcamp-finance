import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        self.cbox = QCheckBox("미수", self)
        self.cbox.move(10, 10)

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()