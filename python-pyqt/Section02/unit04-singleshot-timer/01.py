import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        QTimer.singleShot(5000, self.timeout)

    def timeout(self):
        msg = "프로그램 실행 후 5초 경과"
        self.statusBar().showMessage(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()