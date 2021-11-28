from PyQt5.QtWidgets import QApplication, QGraphicsView, QGridLayout
import sys
import finplot as fplt
import pyupbit

fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000" 
fplt.candle_bear_color = "#0000FF"


class MyWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGraphicsView")
        layout = QGridLayout()
        self.setLayout(layout)
        self.resize(800, 300)

        # ax
        ax = fplt.create_plot(init_zoom_periods=100)
        self.axs = [ax] # finplot requres this property
        layout.addWidget(ax.vb.win, 0, 0)

        df = pyupbit.get_ohlcv("KRW-BTC")
        print(type(df.index))
        df.rename(columns={'open': "Open", "high": "High", "low": "Low", "close":"Close"}, inplace=True)
        fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])

        df['Close'].rolling(5).mean().plot(ax=ax, legend='MA5')
        df['Close'].rolling(20).mean().plot(ax=ax, legend='MA20')
        df['Close'].rolling(60).mean().plot(ax=ax, legend='MA60')

        fplt.show(qt_exec=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow() 
    win.show()
    app.exec_()
