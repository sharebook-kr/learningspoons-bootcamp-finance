import requests
from bs4 import BeautifulSoup
import sqlite3

def get_stock_info(ticker):
    url = f"https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={ticker}"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, 'html5lib')
    sel = "#pArea > div.wrapper-table > div > table > tbody > tr:nth-of-type(3) > td > dl > dt:nth-of-type(3) > b"
    result = soup.select(sel)
    per = float(result[0].text)

    sel = "#pArea > div.wrapper-table > div > table > tbody > tr:nth-of-type(3) > td > dl > dt:nth-of-type(5) > b"
    result = soup.select(sel)
    pbr = float(result[0].text)

    sel = "#pArea > div.wrapper-table > div > table > tbody > tr:nth-of-type(3) > td > dl > dt:nth-of-type(6) > b"
    result = soup.select(sel)
    div = float(result[0].text.replace("%", ""))

    return { "per": per, "pbr": pbr, "div": div}

ticker = "005930"
result = get_stock_info(ticker)

print(result['per'])
print(result['pbr'])
print(result['div'])