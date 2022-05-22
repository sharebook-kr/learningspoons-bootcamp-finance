import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.home_action = QAction(QIcon("home.png"), 'home')
        self.home_action.triggered.connect(self.close)

        self.setting_action = QAction(QIcon("settings.png"), 'settings')
        self.setting_action.triggered.connect(self.setting)

        self.envelope_action = QAction(QIcon("envelope.png"), 'envelope')
        self.envelope_action.triggered.connect(self.envelope)

        self.toolbar = self.addToolBar('title')
        self.toolbar.addAction(self.home_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.setting_action)
        self.toolbar.addAction(self.envelope_action)

    def setting(self):
        print('setting toolbar clicked')

    def envelope(self):
        print('envelope toolbar clicked')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()