import sys 
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import pythoncom
import time
import multiprocessing as mp


class MyWindow(QWidget):
    app = QApplication(sys.argv)

    def __init__(self):
        super().__init__()
        self.login_status = False
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self.slot_login)
        self.login()

    def login(self):
        self.ocx.dynamicCall("CommConnect()")
        while not self.login_status: 
            pythoncom.PumpWaitingMessages()
            time.sleep(0.001)

    def slot_login(self, err_code):
        self.login_status = True
        print("login is complete")


if __name__ == "__main__":
    sub_proc = mp.Process(target=MyWindow, name="Sub Process")
    sub_proc.start()

    for i in range(60):
        print("sleep ", 60-i)
        time.sleep(1)

    if sub_proc.is_alive():
        sub_proc.kill()

    while True:
        print("main process is running")
        time.sleep(1)
