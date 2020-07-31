import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.dynamicCall("CommConnect()")
        self.ocx.OnEventConnect.connect(self.login)

    def login(self, err_code):
        if err_code == 0:
            print("로그인 성공")
        else:
            print("로그인 실패")

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()