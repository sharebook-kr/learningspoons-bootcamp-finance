import ccxt

exchange = ccxt.mexc()
markets = exchange.load_markets()

usdt_markets = []
for ticker in markets:
    name, fiat = ticker.split('/')
    if fiat == 'USDT':
        usdt_markets.append(ticker)

print(len(usdt_markets))