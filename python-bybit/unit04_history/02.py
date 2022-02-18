from pybit import HTTP
import pprint
import pandas as pd

session = HTTP(
    endpoint="https://api.bybit.com", 
    spot=False
)

resp = session.query_kline(
    symbol="BTCUSDT",
    interval=5,
    limit=200,
    from_time=1581231260
)

result = resp['result']
df = pd.DataFrame(result)
ts = pd.to_datetime(df['open_time'], unit='s')
df.set_index(ts, inplace=True)
df = df[['open', 'high', 'low', 'close']]
print(df)