import pyupbit
import pprint

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)

resp = upbit.buy_limit_order("KRW-XRP", 200, 100)
pprint.pprint(resp)