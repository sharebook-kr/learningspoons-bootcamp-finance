import ccxt 
import time
import datetime
import pandas as pd

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

# volatility breakout 
btc = binance.fetch_ohlcv(
    symbol=symbol,
    timeframe='1d', 
    since=None, 
    limit=10)

df = pd.DataFrame(
    data=btc, 
    columns=['datetime', 'open', 'high', 'low', 'close', 'volume']
)
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df.set_index('datetime', inplace=True)

yesterday = df.iloc[-2]
today = df.iloc[-1]
target = today['open'] + (yesterday['high'] - yesterday['low']) * 0.5
print(target)


#while True: 
#    btc = binance.fetch_ticker(symbol)
#    now = datetime.datetime.now()
#    print(now, btc['last'])
#    time.sleep(1)
#
    
