import sys 
from PyQt5.QtWidgets import *
import qdarkstyle

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        btn = QPushButton("button", self)
        btn.move(10, 10)

        label = QLabel("Hello Dark Style", self)
        label.move(10, 100)
        label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    win = MyWindow()
    win.show()
    app.exec_()