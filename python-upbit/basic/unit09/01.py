import pyupbit

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
#print(access)
#print(secret)

upbit = pyupbit.Upbit(access, secret)
balance = upbit.get_balance("KRW")
print(balance)
