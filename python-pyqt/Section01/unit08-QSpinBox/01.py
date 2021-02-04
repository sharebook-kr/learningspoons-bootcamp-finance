import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        self.spin_box = QSpinBox(self)
        self.spin_box.move(10, 10)
        self.spin_box.resize(100, 30)
        self.spin_box.valueChanged.connect(self.slot)

    def slot(self):
        input_val = self.spin_box.value()
        print(input_val)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()