import sys
from PyQt5.QtWidgets import *
import finplot as fplt
import pyupbit

fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000"
fplt.candle_bear_color = "#0000FF"

def tickStrings(self, values, scale, spacing):
    if self.hide_strings:
        return []
    xform = self.vb.yscale.xform
    return [format(xform(value), ',') for value in values]

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget= QGraphicsView()
        layout = QGridLayout(widget)
        self.setCentralWidget(widget)
        self.resize(800, 300)

        ax = fplt.create_plot(init_zoom_periods=100)
        widget.axs = [ax]
        layout.addWidget(ax.vb.win, 0, 0)

        df = pyupbit.get_ohlcv("KRW-BTC")
        fplt.candlestick_ochl(df[['open', 'close', 'high', 'low']])
        fplt.YAxisItem.tickStrings = tickStrings
        axis = ax.axes['right']['item']
        axis.setWidth(100)
        fplt.show(qt_exec=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()