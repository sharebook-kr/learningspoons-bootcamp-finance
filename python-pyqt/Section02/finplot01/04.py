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

        self.edit = QLineEdit("")
        button = QPushButton("Plot")
        button.clicked.connect(self.plot)

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.edit)
        hbox_layout.addWidget(button)
        hbox_layout.addStretch(4)

        widget= QGraphicsView()
        layout = QVBoxLayout(widget)
        self.setCentralWidget(widget)
        self.resize(800, 300)

        self.ax = fplt.create_plot(init_zoom_periods=100)
        self.axs = [self.ax] # finplot requres this property
        self.axo = self.ax.overlay()

        layout.addLayout(hbox_layout)
        layout.addWidget(self.ax.vb.win)

    def plot(self):
        symbol = self.edit.text()
        df = fdr.DataReader(symbol=symbol, start="2021")

        # remove previous plots 
        self.ax.reset() 
        self.axo.reset()

        fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
        fplt.show(qt_exec=False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()