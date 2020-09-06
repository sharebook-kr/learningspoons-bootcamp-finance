import requests
from bs4 import BeautifulSoup

url = "http://consensus.hankyung.com/apps.analysis/analysis.list?sdate=2020-01-01&edate=2020-01-10&now_page=1&search_value=&report_type=CO&pagenum=80&search_text=%C3%D6%C1%D8%BF%B5&business_code="
headers = {
    "User-Agent": "Hello World"
}

resp = requests.get(url, headers=headers)
resp.encoding = "euc-kr"
bs = BeautifulSoup(resp.text, 'html5lib')


sel = "#contents > div.table_style01 > table > tbody > tr > td.first.txt_number"
result = bs.select(sel)
for item in result:
    print(item.text.strip())

sel = "#contents > div.table_style01 > table > tbody > tr > td:nth-child(4)"
result = bs.select(sel)
for item in result:
    print(item.text.strip())

sel = "#content_548015 strong"
result = bs.select(sel)
for item in result:
    print(item.text.strip())
