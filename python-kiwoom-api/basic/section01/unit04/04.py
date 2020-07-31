import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.dynamicCall("CommConnect()")
        self.ocx.OnEventConnect.connect(self.handle_login)

        btn = QPushButton("로그인 정보", self)
        btn.move(10, 10)
        btn.clicked.connect(self.handle_button_clicked)

    def handle_login(self, err_code):
        if err_code == 0:
            self.statusBar().showMessage("로그인 성공")
        else:
            self.statusBar().showMessage("로그인 실패")

    def handle_button_clicked(self):
        accounts = self.ocx.dynamicCall("GetLoginInfo(QString)", "ACCNO")
        print(accounts)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()