from PyQt5.QtWidgets import *
import sys
import kiwoom


class Receiver:
    def __init__(self, queue):
        self.queue = queue
        self.app =  QApplication(sys.argv)
        self.kiwoom = kiwoom.Kiwoom(self.OnReceiveRealCondition)
        self.kiwoom.CommConnect()
        
        # condition
        self.kiwoom.GetConditionLoad()
        self.kiwoom.GetConditionNameList()
        self.kiwoom.SendCondition("100", "golden", 0, 1)

        self.app.exec_()


    def OnReceiveRealCondition(self, code, type, cond_name, cond_index):
        #print(code, type) 
        self.queue.put((code, type))