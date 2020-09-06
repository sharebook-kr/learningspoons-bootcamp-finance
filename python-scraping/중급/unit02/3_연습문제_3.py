import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "html5lib")
sel = "#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a"
result = soup.select(sel)

for item in result:
    print(item.text.strip())