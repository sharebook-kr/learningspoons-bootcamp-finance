import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

app = QApplication(sys.argv)

rect = QGraphicsRectItem()
rect.setRect(10, 10, 50, 50)
rect.setBrush(Qt.yellow)
rect.setPen(QPen(Qt.red, 5))

scene = QGraphicsScene()
scene.addItem(rect)

view = QGraphicsView()
view.setScene(scene)
view.show()

app.exec_()
