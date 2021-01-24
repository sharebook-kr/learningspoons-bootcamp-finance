import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        self.radio1 = QRadioButton(text="당일", parent=self)
        self.radio1.move(10, 10)
        self.radio1.setChecked(True)
        self.radio1.toggled.connect(self.slot)

        self.radio2 = QRadioButton(text="전일", parent=self)
        self.radio2.move(100, 10)

    def slot(self):
        if self.radio1.isChecked():
            print("radio1 is checked")
        else:
            print("radio2 is checked")


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()