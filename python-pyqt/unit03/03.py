import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle("Auto Trading v0.1")
        self.setWindowIcon(QIcon("chart.png"))


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()