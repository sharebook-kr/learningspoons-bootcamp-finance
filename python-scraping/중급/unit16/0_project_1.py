import requests
from bs4 import BeautifulSoup
import sqlite3

con = sqlite3.connect("project.db")
cur = con.cursor()

query = "create table if not exists ticker ( ticker text, name text )"
cur.execute(query)

url = "https://finance.naver.com/sise/sise_market_sum.nhn"

resp = requests.get(url)
print("삼성전자" in resp.text)

soup = BeautifulSoup(resp.text, 'html5lib')
sel = "#contentarea > div.box_type_l > table.type_2 > tbody > tr > td:nth-of-type(2) > a"
result = soup.select(sel)
for item in result:
    ticker = item['href'].split("=")[1]
    name   = item.text
    # print(ticker, name)

    query = f"insert into ticker values ('{ticker}', '{name}')"
    cur.execute(query)

con.commit()
con.close()
