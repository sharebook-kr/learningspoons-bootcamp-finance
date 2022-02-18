import finplot as fplt
import FinanceDataReader as fdr

fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000" 
fplt.candle_bear_color = "#0000FF"

df = fdr.DataReader(symbol="KS11", start="2021")
fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
fplt.show()