import requests
from bs4 import BeautifulSoup

url = "https://www.google.co.kr/search?q=러닝스푼즈"
resp = requests.get(url)

bs = BeautifulSoup(resp.text, 'html5lib')
sel = "#main div div div a div"
result = bs.select(sel)

print(result[0].text)