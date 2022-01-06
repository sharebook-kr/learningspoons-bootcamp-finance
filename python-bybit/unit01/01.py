from pybit import HTTP
import pprint

session = HTTP(
    endpoint="https://api.bybit.com", 
    spot=True
)

symbols = session.query_symbol()
result = symbols['result']
for symbol in result:
    pprint.pprint(symbol)