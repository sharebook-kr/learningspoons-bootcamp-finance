# crosshair
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
    return [format(xform(value), ',.1f') for value in values]

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget= QGraphicsView()
        layout = QVBoxLayout(widget)
        self.setCentralWidget(widget)
        self.resize(800, 400)

        # edit
        hbox = QHBoxLayout()
        self.edit = QLineEdit("KRW-BTC")
        self.button = QPushButton("Plot")
        self.button.clicked.connect(self.update_plot)
        hbox.addWidget(self.edit)
        hbox.addWidget(self.button)
        hbox.addStretch(4)

        self.ax = fplt.create_plot(init_zoom_periods=100)
        widget.axs = [self.ax]
        layout.addLayout(hbox)
        layout.addWidget(self.ax.vb.win)

        self.update_plot()

    def update_plot(self):
        symbol = self.edit.text()
        self.df = pyupbit.get_ohlcv(symbol)
        self.ax.reset()
        self.ax.overlay().reset()
        fplt.candlestick_ochl(self.df[['open', 'close', 'high', 'low']], ax=self.ax)
        self.hover_label = fplt.add_legend('', ax=self.ax)
        fplt.YAxisItem.tickStrings = tickStrings
        axis = self.ax.axes['right']['item']
        axis.setWidth(100)
        fplt.set_time_inspector(self.update_hover_label, ax=self.ax, when='hover')
        fplt.add_crosshair_info(self.update_crosshair_text, ax=self.ax)
        fplt.show(qt_exec=False)

    def update_hover_label(self, x, y):
        timestamp = [int(x.timestamp()) for x in self.df.index]
        epoch = int(x / 1000000000)
        index = timestamp.index(epoch)
        s = self.df.iloc[index]
        text = f"O {s['open']:,} H {s['high']:,} L {s['low']:,} C {s['close']:,}"
        self.hover_label.setText(text)

    def update_crosshair_text(self, x, y, xtext, ytext):
        return xtext, format(y, ",")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()