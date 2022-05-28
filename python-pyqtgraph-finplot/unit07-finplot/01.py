import finplot as fplt
import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
fplt.candlestick_ochl(df[['open', 'close', 'high', 'low']])
fplt.show()