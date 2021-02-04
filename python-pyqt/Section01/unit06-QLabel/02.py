import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        self.label1 = QLabel(self)
        self.label1.resize(300, 30)
        self.label1.move(10, 10)

        self.btn1 = QPushButton("click", self)
        self.btn1.move(10, 50)
        self.btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        self.label1.setText("button clicked")


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()