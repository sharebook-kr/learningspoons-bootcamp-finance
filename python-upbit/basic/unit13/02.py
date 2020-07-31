import pyupbit
import pprint

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)
resp = upbit.cancel_order(uuid='211bad05-767b-4d18-b894-f3de772ee2bb')
print(resp)
