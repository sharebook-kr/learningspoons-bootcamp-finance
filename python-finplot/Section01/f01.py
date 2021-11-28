from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
import sys

class MyWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        #scene = QGraphicsScene()
        #scene.addText("QGraphicsScene")
        #self.setScene(scene)

        self.setWindowTitle("QGraphicsView")
        self.resize(600, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow() 
    win.show()
    app.exec_()