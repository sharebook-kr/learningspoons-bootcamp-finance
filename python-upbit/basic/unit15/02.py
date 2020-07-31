import pyupbit
import time

while True: 
    price = pyupbit.get_current_price("KRW-BTC")
    print(price)
    time.sleep(1)