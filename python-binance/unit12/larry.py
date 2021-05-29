import pandas as pd 

# volatility breakout 
def cal_target(exchange, symbol):
    btc = exchange.fetch_ohlcv(
        symbol=symbol,
        timeframe='1d', 
        since=None, 
        limit=10
    )

    df = pd.DataFrame(data=btc, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)

    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    target = today['open'] + (yesterday['high'] - yesterday['low']) * 0.5
    return target 