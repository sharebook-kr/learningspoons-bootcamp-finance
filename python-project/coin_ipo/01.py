import pyupbit


with open("account.txt") as f:
    lines = f.readlines()
    access = lines[0].strip()
    secret = lines[1].strip()
    print(access, secret)


upbit = pyupbit.Upbit(access, secret)
krw_balance = upbit.get_balance(ticker="KRW")
print(krw_balance)