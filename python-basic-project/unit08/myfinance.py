import requests 
from bs4 import BeautifulSoup

def get_tickers(market=2):
    url = f"http://comp.fnguide.com/SVO2/common/lookup_data.asp?mkt_gb={market}&comp_gb=1"
    resp = requests.get(url)
    data = resp.json()
    codes = []
    for comp in data:
        code = comp['cd'][-6:]
        codes.append(code)
    return codes

def get_dvr(code):
    try:
        url = f"https://finance.naver.com/item/main.nhn?code={code}"
        resp = requests.get(url)
        html = resp.text 

        soup = BeautifulSoup(html, "html5lib")
        tags = soup.select("#_dvr")
        dvr = float(tags[0].text)
    except:
        dvr = 0
    return dvr


if __name__ == "__main__":
    kospi = get_tickers(market=2)
    kosdaq = get_tickers(market=3)
    print(len(kospi))
    print(len(kosdaq))

    print(get_dvr("005930"))