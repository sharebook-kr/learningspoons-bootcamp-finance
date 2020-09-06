import requests
import time

def get_coin_closing_price(ticker):
    url = f"https://api.bithumb.com/public/ticker/{ticker}_KRW"
    resp = requests.get(url)
    data = resp.json()
    return data['data']['closing_price']

while True:
    value = get_coin_closing_price("LTC")
    print(value)
    time.sleep(0.1)
