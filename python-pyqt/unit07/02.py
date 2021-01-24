import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        self.line_edit1 = QLineEdit(self) 
        self.line_edit1.move(10, 10)
        self.line_edit1.resize(200, 30)
        self.line_edit1.textChanged.connect(self.line_edit_slot)

    def line_edit_slot(self):
        user_data = self.line_edit1.text()
        print(user_data)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()