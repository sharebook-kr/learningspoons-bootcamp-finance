import sys 
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        grp_box = QGroupBox("조회날짜", self)

        radio1 = QRadioButton("당일")
        radio2 = QRadioButton("전일")
        radio1.setChecked(True)

        layout = QVBoxLayout()
        layout.addWidget(radio1)
        layout.addWidget(radio2)

        grp_box.setLayout(layout)



app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()