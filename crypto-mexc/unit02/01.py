import ccxt
import pprint

exchange = ccxt.mexc()
btc_usdt = exchange.fetch_ticker("BTC/USDT")
pprint.pprint(btc_usdt)

