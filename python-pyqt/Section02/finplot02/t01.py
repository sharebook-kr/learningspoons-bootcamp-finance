import pyupbit
import datetime
import time


df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="minute1")
print(df)
while True:
    data = pyupbit.get_current_price("KRW-BTC", verbose=True)
    price = data['trade_price']
    timestamp = data['trade_timestamp'] / 1000
    cur_min_timestamp = timestamp - timestamp % (60)
    cur_min_dt = datetime.datetime.fromtimestamp(cur_min_timestamp)

    if cur_min_dt > df.index[-1]:
        df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="minute1")
    else:
        # update last candle
        df.iloc[-1]['close'] = price 
        if price > df.iloc[-1]['high']:
            df.iloc[-1]['high'] = price
        if price < df.iloc[-1]['high']:
            df.iloc[-1]['low'] = price

    time.sleep(1)