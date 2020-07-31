import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

label = QLabel("Hello PyQt")
label.show()

print("exec 호출 전")
app.exec_()
print("exec 호출 후")
