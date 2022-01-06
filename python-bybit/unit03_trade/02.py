# 바이비트 현물 주문 취소
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

order_id = "1059442109764970752"
resp = session.cancel_active_order(
    orderId=order_id
)
pprint.pprint(resp)

