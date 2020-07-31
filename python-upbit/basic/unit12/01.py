import pyupbit
import pprint

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)
resp = upbit.buy_market_order("KRW-XRP", 10000)
pprint.pprint(resp)