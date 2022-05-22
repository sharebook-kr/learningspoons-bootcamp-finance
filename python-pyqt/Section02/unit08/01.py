import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel()
        label.setPixmap(QPixmap("logo.png"))
        #label.setScaledContents(True)
        button = QPushButton("click")

        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.addWidget(label)
        vbox.addWidget(button)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()