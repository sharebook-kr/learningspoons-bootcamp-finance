from PyQt5.QAxContainer import *
import pythoncom 

class Kiwoom:
    def __init__(self, tr_condition_func, real_condition_func):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.login = False
        self.cond = False

        # signal-slot
        self.ocx.OnEventConnect.connect(self.OnEventConnect)
        self.ocx.OnReceiveConditionVer.connect(self.OnReceiveConditionVer)
        self.ocx.OnReceiveTrCondition.connect(tr_condition_func)
        self.ocx.OnReceiveRealCondition.connect(real_condition_func)

    def OnEventConnect(self, code):
        self.login = True   

    def OnReceiveConditionVer(self, ret, msg):
        if ret == 1:
            self.cond = True

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        while self.login is False:
            pythoncom.PumpWaitingMessages()

    def GetConditionLoad(self):
        self.ocx.dynamicCall("GetConditionLoad()")
        while self.cond is False:
            pythoncom.PumpWaitingMessages()

    def GetConditionNameList(self):
        data = self.ocx.dynamicCall("GetConditionNameList()")
        conditions = data.split(";")[:-1]

        condition_list = []
        for cond in conditions:
            index, name = cond.split('^')
            condition_list.append((index, name))
        return condition_list

    def SendCondition(self, screen, cond_name, cond_index, search):
        self.ocx.dynamicCall("SendCondition(QString, QString, int, int)", screen, cond_name, cond_index, search)

    def SendConditionStop(self, screen, cond_name, cond_index):
        self.ocx.dynamicCall("SendConditionStop(QString, QString, int)", screen, cond_name, cond_index)
