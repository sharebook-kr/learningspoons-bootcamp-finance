import sys
from PyQt5.QtWidgets import *
import finplot as fplt
import pyupbit

fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000"
fplt.candle_bear_color = "#0000FF"

fplt.volume_bull_color = "#FF0000"
fplt.volume_bull_body_color = "#FF0000"
fplt.volume_bear_color = "#0000FF"

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget= QGraphicsView()
        layout = QGridLayout(widget)
        self.setCentralWidget(widget)
        self.resize(1200, 600)

        ax0, ax1 = fplt.create_plot_widget(master=widget, rows=2, init_zoom_periods=100)
        widget.axs = [ax0, ax1]
        layout.addWidget(ax0.ax_widget, 0, 0)
        layout.addWidget(ax1.ax_widget, 1, 0)

        #print(type(ax0))
        #print(type(ax0.ax_widget))
        #print(type(ax0.vb))
        #print(type(ax0.vb.win))

        df = pyupbit.get_ohlcv("KRW-BTC")
        fplt.candlestick_ochl(df[['open', 'close', 'high', 'low']], ax=ax0)
        fplt.volume_ocv(df[['open', 'close', 'volume']], ax=ax1)
        fplt.show(qt_exec=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()