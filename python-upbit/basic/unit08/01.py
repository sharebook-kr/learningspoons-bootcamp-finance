import pyupbit
import pprint

orderbooks = pyupbit.get_orderbook("KRW-BTC")
pprint.pprint(orderbooks)