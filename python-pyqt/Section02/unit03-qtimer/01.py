import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication 
from PyQt5.QtCore import QTimer

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        timer = QTimer(self)
        timer.start(1000)           # 1 sec
        timer.timeout.connect(self.display_price)

    def display_price(self):
        print("hello") 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()