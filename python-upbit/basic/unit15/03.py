import pyupbit
import time
import datetime

while True: 
    now = datetime.datetime.now()
    price = pyupbit.get_current_price("KRW-BTC")
    print(now, price)
    time.sleep(1)