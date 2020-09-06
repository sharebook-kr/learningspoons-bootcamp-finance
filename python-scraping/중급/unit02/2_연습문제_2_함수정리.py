import requests
from bs4 import BeautifulSoup

def get_per(ticker):
    url = f"https://finance.naver.com/item/main.nhn?code={ticker}"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, "html5lib")
    sel = "#_per"
    result = soup.select(sel)
    return result[0].text

for ticker in ["005930", "066570", "000660"]:
    per = get_per(ticker)
    print(ticker, per)