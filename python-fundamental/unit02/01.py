# 요구 수익률 스크래핑 
import requests
from bs4 import BeautifulSoup

url = "https://www.kisrating.com/ratingsStatistics/statics_spread.do"
resp = requests.get(url)
html = resp.text 

soup = BeautifulSoup(html, "html5lib")
tag = soup.select("#con_tab1 > div.table_ty1 > table > tbody > tr:nth-child(11) > td:nth-child(9)")
K = float(tag[0].text)
print("할인율: ", K)

