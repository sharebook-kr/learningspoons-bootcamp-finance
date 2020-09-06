import requests
from bs4 import BeautifulSoup
import sqlite3
import time

def get_stock_info(ticker):
    url = f"https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={ticker}"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, 'html5lib')
    sel = "#pArea > div.wrapper-table > div > table > tbody > tr:nth-of-type(3) > td > dl > dt:nth-of-type(3) > b"
    result = soup.select(sel)
    try:
        per = float(result[0].text)
    except:
        per = 0
    sel = "#pArea > div.wrapper-table > div > table > tbody > tr:nth-of-type(3) > td > dl > dt:nth-of-type(5) > b"
    result = soup.select(sel)
    try:
        pbr = float(result[0].text)
    except:
        pbr = 0
    sel = "#pArea > div.wrapper-table > div > table > tbody > tr:nth-of-type(3) > td > dl > dt:nth-of-type(6) > b"
    result = soup.select(sel)
    try:
        div = float(result[0].text.replace("%", ""))
    except:
        div = 0
    return { "per": per, "pbr": pbr, "div": div}

con = sqlite3.connect('project.db')
cur = con.cursor()

query = "create table if not exists fundamental (ticker text, per real, pbr real, div real)"
cur.execute(query)

query = "select * from ticker"
cur.execute(query)
tickers = cur.fetchall()
for t in tickers[:10]:
    ticker = t[0]

    result = get_stock_info(ticker)
    print(result)
    query = f"insert into fundamental values ('{ticker}', {result['per']}, {result['pbr']}, {result['div']})"
    cur.execute(query)

    time.sleep(1)


con.commit()
con.close()

