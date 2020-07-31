import pyupbit

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)
xrp_balance = upbit.get_balance("KRW-XRP")
resp = upbit.sell_limit_order("KRW-XRP", 265, xrp_balance)
print(resp)