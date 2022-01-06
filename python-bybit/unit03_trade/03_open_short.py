from pybit import HTTP
import pprint

with open("../../bybit.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

session = HTTP(
    endpoint="https://api.bybit.com", 
    api_key=api_key, 
    api_secret=api_secret
)

resp = session.place_active_order(
    symbol="XRPUSDT",
    side="Sell",
    order_type="Limit",
    qty=10,
    price=0.8390,
    time_in_force="GoodTillCancel",
    reduce_only=False,
    close_on_trigger=False
)

print(resp)