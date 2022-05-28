import sys
from PyQt5.QtWidgets import *
import finplot as fplt
import pyupbit

fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000"
fplt.candle_bear_color = "#0000FF"


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
        #print(type(ax))
        #print(type(ax.vb))
        #print(type(ax.vb.win))

        df = pyupbit.get_ohlcv("KRW-BTC")
        fplt.candlestick_ochl(df[['open', 'close', 'high', 'low']])
        fplt.show(qt_exec=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()