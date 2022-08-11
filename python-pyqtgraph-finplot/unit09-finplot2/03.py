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

        gv = QGraphicsView()
        layout = QGridLayout(gv)
        self.setCentralWidget(gv)
        self.resize(800, 300)

        ax = fplt.create_plot(init_zoom_periods=100)
        gv.axs = [ax]
        layout.addWidget(ax.vb.win, 0, 0)

        df = pyupbit.get_ohlcv("KRW-BTC")
        fplt.candlestick_ochl(df[['open', 'close', 'high', 'low']])
        df['close'].rolling(5).mean().plot(ax=ax, legend='MA5')
        df['close'].rolling(20).mean().plot(ax=ax, legend='MA20')
        df['close'].rolling(60).mean().plot(ax=ax, legend='MA60')
        fplt.show(qt_exec=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()