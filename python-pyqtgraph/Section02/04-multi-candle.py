import sys
from PyQt5.QtGui import QPainter, QPicture
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRectF, QPointF
import pyqtgraph as pg
import FinanceDataReader as fdr


class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.df = data 
        self.generatePicture()
    
    def generatePicture(self):
        self.picture = QPicture()
        p = QPainter(self.picture)

        for i, index in enumerate(self.df.index): 
            open = self.df.loc[index]['Open']
            high = self.df.loc[index]['High']
            low = self.df.loc[index]['Low']
            close = self.df.loc[index]['Close']

            if close >= open:
                p.setPen(pg.mkPen(color='r'))
                p.setBrush(pg.mkBrush(color='r'))
            else:
                p.setPen(pg.mkPen(color='b'))
                p.setBrush(pg.mkBrush(color='b'))

            p.drawLine(QPointF(i, high), QPointF(i, low))
            p.drawRect(QRectF(i-0.25, open, 0.5, close-open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        return QRectF(self.picture.boundingRect())


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # data 
        df = fdr.DataReader("005930", "2021")

        w = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
        #w = pg.PlotWidget()
        self.setCentralWidget(w)

        # style
        w.setBackground('w')

        # plot
        item = CandlestickItem(df)
        w.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()