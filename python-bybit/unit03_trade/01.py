# 바이비트 현물 지정가 매수 
from pybit import HTTP
import pprint

with open("../../bybit.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

session = HTTP(
    endpoint="https://api.bybit.com", 
    api_key=api_key, 
    api_secret=api_secret,
    spot=True
)

resp = session.place_active_order(
    symbol="XRPUSDT",
    side="Buy",
    type="LIMIT",
    qty=10,
    timeInForce="GTC",
    price=0.83
)
pprint.pprint(resp)

