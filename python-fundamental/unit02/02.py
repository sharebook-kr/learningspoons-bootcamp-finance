# 자본총계(비지배주주지분)
import requests
from bs4 import BeautifulSoup

# html
url = "http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930"
resp = requests.get(url)
html = resp.text 

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#highlight_D_A > table > tbody > tr:nth-child(10) > td:nth-child(4)")
equity = tags[0].text
equity = equity.replace(",", "")
equity = float(equity) * 100000000
print(equity)


