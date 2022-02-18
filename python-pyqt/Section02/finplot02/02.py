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

        view = QGraphicsView()
        grid_layout = QGridLayout(view)
        self.setCentralWidget(view)
        self.resize(1200, 600)

        # ax0, ax1 -> pyqtgraph.graphicsItem.PlotItem
        # ax0.ax_widget -> pyqtgraph.widgets.PlotWidget
        ax0, ax1 = fplt.create_plot_widget(master=view, rows=2, init_zoom_periods=100)
        view.axs = [ax0, ax1]
        grid_layout.addWidget(ax0.ax_widget, 0, 0)
        grid_layout.addWidget(ax1.ax_widget, 1, 0)

        df = fdr.DataReader(symbol="KS11", start="2020")
        ax0.reset()
        ax1.reset()
        fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']], ax=ax0)
        fplt.volume_ocv(df[['Open', 'Close', 'Volume']], ax=ax1)
        fplt.refresh()      # refresh autoscaling when all plots complete
        fplt.show(qt_exec=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()