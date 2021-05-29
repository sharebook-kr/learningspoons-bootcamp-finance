# Set Leverage
# 바이낸스 웹 페이지에 접속한 상태에서 코드를 실행하면 안됨. 
# 모든 바이낸스 접속을 종료한 후 다음 코드를 실행할 것
# 다음 코드가 실행되면 기본적으로 레베러지 설정이 변경되므로 
# 웹 페이지에서 주문시 변경된 레베리지를 확인하고 사용할 것. 
import ccxt 
import pprint


with open("../api.txt") as f:
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


markets = binance.load_markets()
symbol = "BTC/USDT"
market = binance.market(symbol)
leverage = 2 

resp = binance.fapiPrivate_post_leverage({
    'symbol': market['id'],
    'leverage': leverage
})

order = binance.create_market_buy_order(
    symbol=symbol,
    amount=0.001,
)