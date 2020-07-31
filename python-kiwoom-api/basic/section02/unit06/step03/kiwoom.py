import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *


class Kiwoom:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveTrData.connect(self._handler_tr)
        self.ocx.OnReceiveChejanData.connect(self._handler_chejan)
        self.ocx.OnReceiveMsg.connect(self._handler_msg)
        self.ocx.OnReceiveConditionVer.connect(self._handler_condition_load)
        self.ocx.OnReceiveTrCondition.connect(self._handler_tr_condition)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        self.login_loop = QEventLoop()
        self.login_loop.exec()

    def GetLoginInfo(self, tag):
        data = self.ocx.dynamicCall("GetLoginInfo(QString)", tag)
        return data

    def GetCodeListByMarket(self, market):
        data = self.ocx.dynamicCall("GetCodeListByMarket(QString)", market)
        codes = data.split(";")
        return codes[:-1]

    def GetMasterCodeName(self, code):
        data = self.ocx.dynamicCall("GetMasterCodeName(QString)", code)
        return data

    def GetMasterListedStockCnt(self, code):
        data = self.ocx.dynamicCall("GetMasterListedStockCnt(QString)", code)
        return data

    def GetMasterListedStockDate(self, code):
        data = self.ocx.dynamicCall("GetMasterListedStockDate(QString)", code)
        return data

    def GetMasterLastPrice(self, code):
        data = self.ocx.dynamicCall("GetMasterLastPrice(QString)", code)
        return int(data)

    def GetMasterConstruction(self, code):
        data = self.ocx.dynamicCall("GetMasterConstruction(QString)", code)
        return data

    def GetMasterStockState(self, code):
        data = self.ocx.dynamicCall("GetMasterStockState(QString)", code)
        return data

    def GetThemeGroupList(self, type):
        data = self.ocx.dynamicCall("GetThemeGroupList(int)", type)
        tokens = data.split(';')

        data_dic = {}
        for theme in tokens:
            code, name = theme.split('|')
            if type == 0:
                data_dic[code] = name
            else:
                data_dic[name] = code

        return data_dic

    def GetThemeGroupCode(self, theme_code):
        data = self.ocx.dynamicCall("GetThemeGroupCode(QString)", theme_code)
        tokens = data.split(';')
        return tokens

    def SetInputValue(self, id, value):
        self.ocx.dynamicCall("SetInputValue(QString, QString)", id, value)

    def CommRqData(self, rqname, trcode, next, screen):
        self.ocx.dynamicCall("CommRqData(QString, QString, int, QString)", rqname, trcode, next, screen)
        self.tr_loop = QEventLoop()
        self.tr_loop.exec()

    def GetCommData(self, trcode, rqname, index, item):
        data = self.ocx.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, index, item)
        return data.strip()

    def _handler_login(self, err):
        self.login_loop.exit()

    def GetRepeatCnt(self, trcode, rqname):
        ret = self.ocx.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        return ret

    def SendOrder(self, rqname, screen, accno, order_type, code, quantity, price, hoga, order_no):
        self.ocx.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                             [rqname, screen, accno, order_type, code, quantity, price, hoga, order_no])
        self.order_loop = QEventLoop()
        self.order_loop.exec()

    def GetChejanData(self, fid):
        data = self.ocx.dynamicCall("GetChejanData(int)", fid)
        return data

    def _handler_tr(self, screen, rqname, trcode, record, next):
        print("OnReceiveTrData: ", screen, rqname, trcode, record, next)
        # TR 데이터 가져가기
        if rqname == "opt10081":
            self._opt10081(rqname, trcode)

        try:
            self.tr_loop.exit()
        except:
            pass

    def _handler_chejan(self, gubun, item_cnt, fid_list):
        print("OnReceiveChejanData", gubun, item_cnt, fid_list)

    def _handler_msg(self, screen, rqname, trcode, msg):
        print("OnReceiveMsg: ", screen, rqname, trcode, msg)

    def _opt10081(self, rqname, trcode):
        rows = self.GetRepeatCnt(trcode, rqname)
        for i in range(rows):
            date = self.GetCommData(trcode, rqname, i, "일자")
            open = self.GetCommData(trcode, rqname, i, "시가")
            high = self.GetCommData(trcode, rqname, i, "고가")
            low = self.GetCommData(trcode, rqname, i, "저가")
            close = self.GetCommData(trcode, rqname, i, "현재가")
            volume = self.GetCommData(trcode, rqname, i, "거래량")
            print(date, open, high, low, close, volume)

    def GetConditionLoad(self):
        self.ocx.dynamicCall("GetConditionLoad()")
        # 사용자 조건식 저장 이벤트까지 대기
        self.condition_load_loop = QEventLoop()
        self.condition_load_loop.exec()

    def _handler_condition_load(self, ret, msg):
        print("OnReceiveConditionVer: ", ret, msg)
        self.condition_load_loop.exit()

    def GetConditionNameList(self):
        data = self.ocx.dynamicCall("GetConditionNameList()")
        conditions = data.split(";")[:-1]

        ret = []
        for condition in conditions:
            index, name = condition.split('^')
            ret.append((index, name))

        return ret

    def SendCondition(self, screen, cond_name, cond_index, search):
        ret = self.ocx.dynamicCall("SendCondition(QString, QString, int, int)", screen, cond_name, cond_index, search)
        self.condition_tr_loop = QEventLoop()
        self.condition_tr_loop.exec()

    def _handler_tr_condition(self, screen, codelist, cond_name, cond_index, next):
        codes = codelist.split(';')
        self.condition_codes = codes[:-1]
        self.condition_tr_loop.exit()


app = QApplication(sys.argv)
