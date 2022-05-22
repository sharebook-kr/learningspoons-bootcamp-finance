import sys
from PyQt5.QtWidgets import *
import datetime


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Log")
        self.text = QPlainTextEdit()
        self.button = QPushButton("click")
        self.button.clicked.connect(self.button_clicked)

        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.addWidget(self.label)
        vbox.addWidget(self.text)
        vbox.addWidget(self.button)
        self.setCentralWidget(widget)

    def button_clicked(self):
        now = datetime.datetime.now()
        fmt = now.strftime("%Y-%m-%d %H:%M:%S")
        self.text.appendPlainText(fmt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()