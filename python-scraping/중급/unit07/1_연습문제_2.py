import requests
from bs4 import BeautifulSoup

def get_report_info(start, end, reporter) :
    url = "http://consensus.hankyung.com/apps.analysis/analysis.list"

    url = "http://consensus.hankyung.com/apps.analysis/analysis.list"
    params = {
        "sdate": start,
        "edate": end,
        "now_page": 1,
        "search_value": "",
        "report_type": "CO",
        "pagenum":80,
        "search_text": reporter.encode('EUC-KR')
    }

    headers = {
        "User-Agent": "Hello World"
    }

    resp = requests.get(url, headers=headers, params=params)
    resp.encoding = "euc-kr"
    bs = BeautifulSoup(resp.text, 'html5lib')

    date = []
    sel = "#contents > div.table_style01 > table > tbody > tr > td:nth-child(1)"
    result = bs.select(sel)
    for item in result:
        date.append(item.text.strip())

    price = []
    sel = "#contents > div.table_style01 > table > tbody > tr > td:nth-child(3)"
    result = bs.select(sel)
    for item in result:
        price.append(item.text.strip())

    opinion = []
    sel = "#contents > div.table_style01 > table > tbody > tr > td:nth-child(4)"
    result = bs.select(sel)
    for item in result:
        opinion.append(item.text.strip())

    return [date, price, opinion]

result = get_report_info("2020-01-01", "2020-01-20", "최준영")
print(result)