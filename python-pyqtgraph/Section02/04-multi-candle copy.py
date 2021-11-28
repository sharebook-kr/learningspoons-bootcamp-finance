import sys
from PyQt5.QtGui import QPainter, QPicture
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRectF, QPointF
import pyqtgraph as pg
import FinanceDataReader as fdr
from pyqtgraph.graphicsItems.DateAxisItem import DateAxisItem, YEAR_MONTH_ZOOM_LEVEL
import time


class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.df = data 
        self.generatePicture()
    
    def generatePicture(self):
        self.picture = QPicture()
        p = QPainter(self.picture)

        #a = pg.DateAxisItem(orientation='bottom')
        for i, index in enumerate(self.df.index): 
            #print(i)
            unix_ts = index.timestamp()
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


#class MyDateAxisItem(pg.DateAxisItem):
#    def __init__(self, orientation, *args, **kwargs):
#        super().__init__(orientation=orientation, *args, **kwargs)
#        self.ts = kwargs['ts']
#
#    def tickStrings(self, values, scale, spacing):
#        #values = self.ts
#        #print(len(self.ts))
#        print(values, scale, spacing)
#        unix_ts = [ self.ts[int(i)] for i in values[:-1]]
#        print(unix_ts)
#        spacing = 5 * 3600 * 24 
#        return super().tickStrings(unix_ts, scale, spacing)

#class MyDateAxisItem(pg.DateAxisItem):
import datetime
class MyDateAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timestamp = kwargs['ts']
        print(self.timestamp)

    def tickStrings(self, values, scale, spacing):
        #print(values, scale, spacing)
        data = [x.strftime("%Y-%m-%d") for x in self.timestamp]
        print(data)
        return data[:3]


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # data 
        df = fdr.DataReader("005930", "2021")

        # trick
        #w1 = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
        unix_ts = [x.timestamp() for x in df.index]
        #w1.plot(x=unix_ts, y=df['Close'])
        #w1_axis = w1.getAxis('bottom')

        # layout
        #dx = [(i, str(v)) for i, v in enumerate(df.index)]
        #axis = pg.DateAxisItem(orientation='bottom')
        axis = MyDateAxisItem(orientation='bottom', ts=df.index)
        #axis = MyDateAxisItem(orientation='bottom', ts=unix_ts)
        #axis.setRange(0, 20)
        #axis.setTicks([dx, []])

        #w = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
        w = pg.PlotWidget(axisItems={'bottom': axis})
        #w = pg.PlotWidget(axisItems={'bottom': w1_axis})
        #w = pg.PlotWidget()
        self.setCentralWidget(w)

        # style
        w.setBackground('w')

        # plot
        #plot_item = w.getPlotItem()
        #view = plot_item.vb
        #axis.linkToView(view)
        #a = plot_item.axes['bottom']['item']
        #print(a)
        #w.getAxis('bottom').setTicks()
        #w.setXRange(0, 20)
        item = CandlestickItem(df)
        w.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()