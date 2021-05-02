import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit 


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # layout 
        layout = QHBoxLayout()
        btn1 = QPushButton("조회 시작")
        btn2 = QPushButton("조회 중지")
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        # widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

    def btn2_clicked(self):
        try:
            self.timer.stop()
        except:
            pass

    def timeout(self):
        btc = pyupbit.get_current_price("KRW-BTC")
        self.statusBar().showMessage(str(btc))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()