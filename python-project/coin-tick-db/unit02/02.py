import multiprocessing as mp
import pyupbit
import datetime


if __name__ == "__main__":
    krw_tickers = pyupbit.get_tickers(fiat="KRW")
    queue = mp.Queue()
    proc = mp.Process(
        target=pyupbit.WebSocketClient,
        args=('ticker', krw_tickers, queue),
        daemon=True
    )
    proc.start()

    while True:
        data = queue.get()
        code = data['code']
        open = data['opening_price']
        high = data['high_price']
        low  = data['low_price']
        close = data['trade_price']
        ts = data['trade_timestamp']
        acc_volume = data['acc_trade_volume']
        acc_price = data['acc_trade_price']
        acc_ask_volume = data['acc_ask_volume']
        acc_bid_volume = data['acc_bid_volume']
        change_rate = data['signed_change_rate']

        dt = datetime.datetime.fromtimestamp(ts/1000)
        print(dt, code, open, high, low, close, acc_volume, acc_price, change_rate)
