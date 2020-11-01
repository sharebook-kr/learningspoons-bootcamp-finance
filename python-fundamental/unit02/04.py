# 유통주식수 scarapping 
# 발행주식수 - 자기주식수(보통주)
import requests
from bs4 import BeautifulSoup

url = "http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A000020"
resp = requests.get(url)
html = resp.text 

selector = "#svdMainGrid1 > table > tbody > tr:nth-child(7) > td:nth-child(2)"
soup = BeautifulSoup(html, "html5lib")
tags = soup.select(selector)
shares = tags[0].text.split('/')[0]
print(shares)

selector = "#svdMainGrid5 > table > tbody > tr:nth-child(5) > td:nth-child(3)"
tags = soup.select(selector)
print(tags[0].text)