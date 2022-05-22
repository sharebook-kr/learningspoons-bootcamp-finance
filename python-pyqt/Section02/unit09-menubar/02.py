import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)

        # file menu action
        self.new_action = QAction("New")
        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.close)

        # help menu action
        self.doc_action = QAction("Documentation")
        self.release_action = QAction("Release Notes")
        self.license_action = QAction("View License")

        # file menu
        file_menu = self.menubar.addMenu("파일")
        file_menu.addAction(self.new_action)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)

        # help menu
        help_menu = self.menubar.addMenu("도움말")
        help_menu.addAction(self.doc_action)
        help_menu.addAction(self.release_action)
        help_menu.addAction(self.license_action)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()