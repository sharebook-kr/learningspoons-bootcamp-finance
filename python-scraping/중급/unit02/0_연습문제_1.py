import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "html5lib")
sel = "#_per"
result = soup.select(sel)

for item in result:
    print(item.text)