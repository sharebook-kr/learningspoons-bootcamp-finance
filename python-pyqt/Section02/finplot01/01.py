import finplot as fplt
import FinanceDataReader as fdr

df = fdr.DataReader(symbol="KS11", start="2021")
fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
fplt.show()