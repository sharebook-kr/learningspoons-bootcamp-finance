import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        print("paintEvent", event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()