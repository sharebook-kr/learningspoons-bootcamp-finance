import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Kiwoom VI 발동 테스트")

        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveTrData.connect(self._handler_tr)
        self.ocx.OnReceiveRealData.connect(self._handler_real_data)
        self.CommConnect()
        
    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")

    def request_vi(self):
        self.SetInputValue("시장구분", "000")
        self.SetInputValue("장전구분", "1")
        self.SetInputValue("종목코드", "")
        self.SetInputValue("발동구분", "1")
        self.SetInputValue("제외종목", "111111011")
        self.SetInputValue("거래량구분", "0")
        #self.SetInputValue("최소거래량", "0")
        #self.SetInputValue("최대거래량", "0")
        self.SetInputValue("거래대금구분", "0")
        #self.SetInputValue("최소거래대금", "0")
        #self.SetInputValue("최대거래대금", "0")
        self.SetInputValue("발동방향", "0")
        self.CommRqData("opt10054", "opt10054", 0, "1000")

    def _handler_login(self, err_code):
        print("handler login", err_code);
        self.request_vi()

    def _handler_tr(self, screen, rqname, trcode, record, next):
        print("OnReceiveTrData: ", screen, rqname, trcode, record, next)
 
    def _handler_real_data(self, code, real_type, real_data):
        #print("OnReceiveRealData", code, real_type, real_data)
        if real_type == "VI발동/해제":
            code = self.GetCommRealData(code, 9001) 
            name = self.GetCommRealData(code, 302) 
            vi_type = self.GetCommRealData(code, 9068) 
            gubun = self.GetCommRealData(code, 9075) 
            print(code, name, vi_type, gubun)

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