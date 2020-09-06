import requests
from bs4 import BeautifulSoup

url = "https://finance.daum.net/"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "html5lib")
sel = "#boxTodayNews > div.imgB.f_clear > div.txtB > a.tit"
result = soup.select(sel)

for item in result:
    print(item.text.strip())