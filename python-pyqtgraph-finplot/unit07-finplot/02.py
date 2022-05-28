import finplot as fplt
import pyupbit

fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000"
fplt.candle_bear_color = "#0000FF"

df = pyupbit.get_ohlcv("KRW-BTC")
fplt.candlestick_ochl(df[['open', 'close', 'high', 'low']])
fplt.show()