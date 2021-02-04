import sys 
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        btn1 = QPushButton("Button1")
        btn2 = QPushButton("Button2")

        layout = QHBoxLayout()
        layout.addStretch(1)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(layout)
        vbox.addStretch(1)

        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()