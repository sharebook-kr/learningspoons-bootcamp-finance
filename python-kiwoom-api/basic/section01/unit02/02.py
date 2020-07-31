import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Bitcoin: ", self)
        self.label.move(10, 10)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(80, 10)
        self.line_edit.resize(100, 30)

        self.btn = QPushButton("조회", self)
        self.btn.move(10, 50)
        self.btn.clicked.connect(self.handle_button)

    def handle_button(self):
        self.line_edit.setText("버튼클릭")



app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
