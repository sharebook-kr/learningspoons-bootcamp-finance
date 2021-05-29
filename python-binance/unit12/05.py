import ccxt 
import pprint
import time
import datetime
import pandas as pd
import larry 

with open("../api.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret  = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key, 
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

symbol = "BTC/USDT"
target = larry.cal_target(binance, symbol)

while True: 
    now = datetime.datetime.now()

    # udpate target price
    if now.hour == 9 and now.minute == 0 and (20 <= now.second < 30):
        target = larry.cal_target(binance, symbol)

    btc = binance.fetch_ticker(symbol)
    print(now, btc['last'])
    time.sleep(1)

    
