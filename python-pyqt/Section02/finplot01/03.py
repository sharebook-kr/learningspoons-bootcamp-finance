import sys 
from PyQt5.QtWidgets import *
import finplot as fplt
import FinanceDataReader as fdr

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

        ax = fplt.create_plot(init_zoom_periods=100)            # pygtgraph.graphicsItems.PlotItem
        axo = ax.overlay()                                      # pygtgraph.graphicsItems.PlotItem
        self.axs = [ax]                                         # finplot requres this property
        layout.addWidget(ax.vb.win, 0, 0)                       # ax.vb     (finplot.FinViewBox)
                                                                # ax.vb.win (finplot.FinWindow)
        df = fdr.DataReader(symbol="KS11", start="2021")
        fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
        fplt.show(qt_exec=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()