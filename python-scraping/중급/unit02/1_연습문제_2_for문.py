import requests
from bs4 import BeautifulSoup

for ticker in ["005930", "066570", "000660"]:
    url = f"https://finance.naver.com/item/main.nhn?code={ticker}"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, "html5lib")
    sel = "#_per"
    result = soup.select(sel)

    for item in result:
        print(ticker, item.text)