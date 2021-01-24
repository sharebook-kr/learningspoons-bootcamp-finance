import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        self.cbox = QCheckBox("미수", self)
        self.cbox.move(10, 10)
        self.cbox.stateChanged.connect(self.slot)

    def slot(self, state):
        if state == Qt.Checked:
            print("미수") 
        else:
            print("보통")

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()