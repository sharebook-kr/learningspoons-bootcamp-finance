from PyQt5.QtWidgets import *
import sys
import kiwoom


class Receiver:
    def __init__(self, queue):
        self.queue = queue
        self.app =  QApplication(sys.argv)
        self.kiwoom = kiwoom.Kiwoom(
            self.OnReceiveTrCondition,
            self.OnReceiveRealCondition
        )
        self.kiwoom.CommConnect()
        
        # condition
        self.kiwoom.GetConditionLoad()
        condition = self.kiwoom.GetConditionNameList()
        for index, name in condition:
            print(index, name)
        self.kiwoom.SendCondition("100", "golden", 0, 1)

        self.app.exec_()

    def OnReceiveTrCondition(self, screen, codelist, cond_name, cond_index, next):
        codes = codelist.split(';')[:-1]
        self.queue.put(codes)

    def OnReceiveRealCondition(self, code, type, cond_name, cond_index):
        #print(code, type) 
        self.queue.put((code, type, cond_name, cond_index))