import pyupbit
import pprint

orderbooks = pyupbit.get_orderbook("KRW-BTC")
orderbook = orderbooks[0]
total_ask_size = orderbook['total_ask_size']
total_bid_size = orderbook['total_bid_size']

print("매도호가 총합: ", total_ask_size)
print("매수호가 총합: ", total_bid_size)
