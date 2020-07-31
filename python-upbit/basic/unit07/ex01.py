import pyupbit

tickers = pyupbit.get_tickers(fiat="KRW")
prices = pyupbit.get_current_price(tickers)

for k, v in prices.items():
    print(k, v)