import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Log")
        self.text = QPlainTextEdit()
        self.button = QPushButton("click")

        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.addWidget(self.label)
        vbox.addWidget(self.text)
        vbox.addWidget(self.button)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()