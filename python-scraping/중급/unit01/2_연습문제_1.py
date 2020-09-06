import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "html5lib")
sel = "#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li > a"
result = soup.select(sel)

for item in result:
    print(item.text)