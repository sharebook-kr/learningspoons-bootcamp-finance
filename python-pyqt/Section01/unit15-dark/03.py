import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        btn = QPushButton("button", self)
        btn.move(10, 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    color_bg_bc = QColor(40, 40, 45)
    color_fg_bc = QColor(190, 190, 195)
    color_bg_dk = QColor(30, 30, 35)
    color_fg_bk = QColor(110, 110, 115)
    color_fg_hl = QColor(175, 175, 180)
    color_bg_bk = QColor(20, 20, 25)

    palette = QPalette()
    palette.setColor(QPalette.Window, color_bg_bc)
    palette.setColor(QPalette.Background, color_bg_bc)
    palette.setColor(QPalette.WindowText, color_fg_bc)
    palette.setColor(QPalette.Base, color_bg_bc)
    palette.setColor(QPalette.AlternateBase, color_bg_dk)
    palette.setColor(QPalette.Text, color_fg_bc)
    palette.setColor(QPalette.Button, color_bg_bc)
    palette.setColor(QPalette.ButtonText, color_fg_bc)
    palette.setColor(QPalette.Link, color_fg_bk)
    palette.setColor(QPalette.Highlight, color_fg_hl)
    palette.setColor(QPalette.HighlightedText, color_bg_bk)
    app.setPalette(palette)
    win = MyWindow()
    win.show()
    app.exec_()