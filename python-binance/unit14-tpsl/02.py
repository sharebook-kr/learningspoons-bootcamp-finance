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
price = 19400

# limit price
orders[0] = binance.create_order(
    symbol="BTC/USDT",
    type="LIMIT",
    side="buy",
    amount=0.001,
    price=price
)

# take profit
orders[1] = binance.create_order(
    symbol="BTC/USDT",
    type="TAKE_PROFIT",
    side="sell",
    amount=0.001,
    price=price,
    params={'stopPrice': 19600}
)

# stop loss
orders[2] = binance.create_order(
    symbol="BTC/USDT",
    type="STOP",
    side="sell",
    amount=0.001,
    price=price,
    params={'stopPrice': 19200}
)

for order in orders:
    pprint.pprint(order)