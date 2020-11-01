# ROE scarapping 
import requests
from bs4 import BeautifulSoup

url = "http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930"
resp = requests.get(url)
html = resp.text 

soup = BeautifulSoup(html, "html5lib")
roe1 = soup.select("#highlight_D_A > table > tbody > tr:nth-child(18) > td:nth-child(2)")[0]
roe2 = soup.select("#highlight_D_A > table > tbody > tr:nth-child(18) > td:nth-child(3)")[0]
roe3 = soup.select("#highlight_D_A > table > tbody > tr:nth-child(18) > td:nth-child(4)")[0]

roe1 = float(roe1.text)
roe2 = float(roe2.text)
roe3 = float(roe3.text)

print(roe1, roe2, roe3)