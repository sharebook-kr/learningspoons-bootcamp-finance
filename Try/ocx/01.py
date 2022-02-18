import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *

app = QApplication(sys.argv)
ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
