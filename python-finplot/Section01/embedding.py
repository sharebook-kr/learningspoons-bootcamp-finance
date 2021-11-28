import finplot as fplt
import FinanceDataReader as fdr 
import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000" 
fplt.candle_bear_color = "#0000FF"

df = fdr.DataReader(symbol="KS11", start="2021")

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle("Auto Trading v0.1")
        self.setWindowIcon(QIcon("chart.png"))

        win = QGraphicsView()
        ax = fplt.create_plot()
        win.axs = [ax]

        fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
        fplt.show()

        self.setCentralWidget(win)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()