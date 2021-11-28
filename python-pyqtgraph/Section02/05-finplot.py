import finplot as fplt
import yfinance

df = yfinance.download('AAPL')
fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
fplt.show()