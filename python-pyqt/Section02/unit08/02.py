import sys
from tkinter import W
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        list_widget = QListWidget()
        list_widget.addItems(["Python 3.7", "Python 3.8", "Python 3.9"])
        list_widget.currentItemChanged.connect(self.item_changed)

        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.addWidget(list_widget)
        self.setCentralWidget(widget)

    def item_changed(self, item):
        print(item.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()