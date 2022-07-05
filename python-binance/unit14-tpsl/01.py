import ccxt
import pprint

with open("../../binance.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret  = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

orders = [None] * 3

# market price (ex: 19500$)
orders[0] = binance.create_order(
    symbol="BTC/USDT",
    type="MARKET",
    side="buy",
    amount=0.001
)

# take profit
orders[1] = binance.create_order(
    symbol="BTC/USDT",
    type="TAKE_PROFIT_MARKET",
    side="sell",
    amount=0.001,
    params={'stopPrice': 19700}
)

# stop loss
orders[2] = binance.create_order(
    symbol="BTC/USDT",
    type="STOP_MARKET",
    side="sell",
    amount=0.001,
    params={'stopPrice': 19300}
)

for order in orders:
    pprint.pprint(order)