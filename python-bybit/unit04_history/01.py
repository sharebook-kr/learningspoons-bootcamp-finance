from pybit import HTTP

session = HTTP(
    endpoint="https://api.bybit.com", 
    spot=False
)

resp = session.query_kline(
    symbol="BTCUSDT",
    interval=1,
    limit=2,
    from_time=1581231260
)
