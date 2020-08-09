# 코스닥 KODEX ETF150 변동성 돌파
import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import datetime


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("코스닥 ETF150 변동성 돌파")

        self.range = None
        self.target = None
        self.account = None
        self.amount = None
        self.hold = None

        self.plain_text_edit = QPlainTextEdit(self)
        self.plain_text_edit.setReadOnly(True)
        self.plain_text_edit.move(10, 10)
        self.plain_text_edit.resize(380, 280)

        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveTrData.connect(self._handler_tr_data)
        self.ocx.OnReceiveRealData.connect(self._handler_real_data)
        self.CommConnect()

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")

    def GetLoginInfo(self, tag):
        data = self.ocx.dynamicCall("GetLoginInfo(QString)", tag)
        return data

    def _handler_login(self, err_code):
        if err_code == 0:
            self.plain_text_edit.appendPlainText("로그인 완료")

            accounts = self.GetLoginInfo("ACCNO")
            self.account = accounts.split(';')[0]

            # TR 요청 
            self.request_opt10081()
            self.request_opw00001()

            # 주식체결 (실시간)
            self.subscribe_stock_conclusion('2')

    def _handler_tr_data(self, screen_no, rqname, trcode, record, next):
        if rqname == "KODEX일봉데이터":
            일자 = self.GetCommData(trcode, rqname, 0, "일자")
            고가 = self.GetCommData(trcode, rqname, 0, "고가")
            저가 = self.GetCommData(trcode, rqname, 0, "저가")
            self.range = int(고가) - int(저가)
            info = f"일자: {일자} 고가: {고가} 저가: {저가}"
            self.plain_text_edit.appendPlainText(info)
        elif rqname == "예수금조회":
            주문가능금액 = self.GetCommData(trcode, rqname, 0, "주문가능금액")
            주문가능금액 = int(주문가능금액)
            self.amount = int(주문가능금액 * 0.2)
            self.plain_text_edit.appendPlainText(f"투자금액: {self.amount}")

    def request_opt10081(self):
        now = datetime.datetime.now()
        today = now.strftime("%Y%m%d")
        self.SetInputValue("종목코드", "229200")
        self.SetInputValue("기준일자", today)
        self.SetInputValue("수정주가구분", 1)
        self.CommRqData("KODEX일봉데이터", "opt10081", 0, "9000")

    def request_opw00001(self):
        self.SetInputValue("계좌번호", self.account)
        self.SetInputValue("비밀번호", "")
        self.SetInputValue("비밀번호입력매체구분", "00")
        self.SetInputValue("조회구분", 2)
        self.CommRqData("예수금조회", "opw00001", 0, "9001")

    # 실시간 타입을 위한 메소드
    def SetRealReg(self, screen_no, code_list, fid_list, real_type):
        self.ocx.dynamicCall("SetRealReg(QString, QString, QString, QString)", 
                              screen_no, code_list, fid_list, real_type)

    def GetCommRealData(self, code, fid):
        data = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, fid) 
        return data

    def DisConnectRealData(self, screen_no):
        self.ocx.dynamicCall("DisConnectRealData(QString)", screen_no)

    # 실시간 이벤트 처리 핸들러 
    def _handler_real_data(self, code, real_type, real_data):
        if real_type == "주식체결":
            시가 = self.GetCommRealData(code, 16)
            시가 = abs(int(시가))          # +100, -100
            현재가 = self.GetCommRealData(code, 10)
            현재가 = abs(int(현재가))          # +100, -100
            self.target = int(시가 + (self.range) * 0.5)      
            self.plain_text_edit.appendPlainText(f"목표가: {self.target}")

            # 매수 
            if self.hold is None and 현재가 > self.target:
                self.hold = True 
                quantity = int(self.amount / 현재가)
                self.SendOrder("매수", "8000", self.account, 1, "229200", quantity, 0, "03", "")

    def subscribe_stock_conclusion(self, screen_no):
        self.SetRealReg(screen_no, "229200", "20", 0)
        self.plain_text_edit.appendPlainText("주식체결 구독신청")

    # TR 요청을 위한 메소드
    def SetInputValue(self, id, value):
        self.ocx.dynamicCall("SetInputValue(QString, QString)", id, value)

    def CommRqData(self, rqname, trcode, next, screen_no):
        self.ocx.dynamicCall("CommRqData(QString, QString, int, QString)", 
                              rqname, trcode, next, screen_no)

    def GetCommData(self, trcode, rqname, index, item):
        data = self.ocx.dynamicCall("GetCommData(QString, QString, int, QString)", 
                                     trcode, rqname, index, item)
        return data.strip()

    def SendOrder(self, rqname, screen, accno, order_type, code, quantity, price, hoga, order_no):
        self.ocx.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                             [rqname, screen, accno, order_type, code, quantity, price, hoga, order_no])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()