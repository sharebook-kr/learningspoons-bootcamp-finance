import pyupbit

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)
balance = upbit.get_balance(ticker="KRW")
print(balance)