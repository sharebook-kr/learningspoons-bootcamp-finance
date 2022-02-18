from pybit import HTTP
import pandas as pd
import time 
import datetime

now = datetime.datetime.now()
today = datetime.datetime(
    year=now.year,
    month=now.month,
    day=now.day,
    hour=0,
    minute=0,
    second=0
)
delta = datetime.timedelta(days=-200)
dt = today + delta 
from_time = time.mktime(dt.timetuple())

session = HTTP(
    endpoint="https://api.bybit.com", 
    spot=False
)

resp = session.query_kline(
    symbol="BTCUSDT",
    interval="D",
    limit=200,
    from_time=from_time
)

result = resp['result']
df = pd.DataFrame(result)
ts = pd.to_datetime(df['open_time'], unit='s')
df.set_index(ts, inplace=True)
df = df[['open', 'high', 'low', 'close']]
print(df)