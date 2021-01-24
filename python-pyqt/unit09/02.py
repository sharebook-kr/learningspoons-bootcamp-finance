import sys 
from PyQt5.QtWidgets import *

item_list = ["보통", "시장가", "조건부지정가"]

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        self.combo = QComboBox(self)
        self.combo.resize(200, 30)
        self.combo.move(10, 10)
        self.combo.addItems(item_list)

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()