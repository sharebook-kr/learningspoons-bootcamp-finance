import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Kiwoom Sector Index 테스트")

        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveTrData.connect(self._handler_tr)
        self.ocx.OnReceiveRealData.connect(self._handler_real_data)
        self.CommConnect()
        
    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")

    def request_sector_index(self):
        self.SetInputValue("시장구분", "0")
        self.SetInputValue("업종코드", "001")

        self.CommRqData("opt20001", "opt20001", 0, "1000")

    def _handler_login(self, err_code):
        print("handler login", err_code);
        self.request_sector_index()

    def _handler_tr(self, screen, rqname, trcode, record, next):
        print("OnReceiveTrData: ", screen, rqname, trcode, record, next)
 
    def _handler_real_data(self, code, real_type, real_data):
        if real_type == "업종지수":
            code = self.GetCommRealData(code, 20) 
            open = self.GetCommRealData(code, 16) 
            high = self.GetCommRealData(code, 17) 
            low  = self.GetCommRealData(code, 18) 
            close= self.GetCommRealData(code, 10)
            print(code, open, high, low, close)

    def SetInputValue(self, id, value):
        self.ocx.dynamicCall("SetInputValue(QString, QString)", id, value)

    def CommRqData(self, rqname, trcode, next, screen):
        self.ocx.dynamicCall("CommRqData(QString, QString, int, QString)", rqname, trcode, next, screen)

    def GetCommData(self, trcode, rqname, index, item):
        data = self.ocx.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, index, item)
        return data.strip()

    def GetCommRealData(self, code, fid):
        data = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, fid) 
        return data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()