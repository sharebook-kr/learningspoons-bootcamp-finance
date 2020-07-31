import pyupbit
import time

while True:
    orderbooks = pyupbit.get_orderbook("KRW-BTC")
    orderbook = orderbooks[0]

    units = orderbook['orderbook_units']
    hoga1 = units[0]

    print(hoga1['ask_price'])
    print(hoga1['bid_price'])

    time.sleep(1)
