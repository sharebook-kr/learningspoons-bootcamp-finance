import ccxt 
import pprint
import time
import datetime
import pandas as pd
import larry 
import math


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
long_target, short_target = larry.cal_target(binance, symbol)
balance = binance.fetch_balance()
usdt = balance['total']['USDT']
op_mode = False 
position = {
    "type": None,
    "amount": 0
} 


def cal_amount(usdt_balance, cur_price):
    portion = 0.1 
    usdt_trade = usdt_balance * portion
    amount = math.floor((usdt_trade * 1000000)/cur_price) / 1000000
    return amount 


ticker = binance.fetch_ticker(symbol)
cur_price = ticker['last']
 
amount = cal_amount(usdt, cur_price)
print(usdt)
print(cur_price)
print(amount)