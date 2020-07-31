import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *

class Kiwoom:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")


app = QApplication(sys.argv)
