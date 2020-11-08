import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 영업이익
def get_operating_profit(code):
    try:
        # download html
        url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode={code}"
        resp = requests.get(url)
        html = resp.text 

        # scarping by css selector
        soup = BeautifulSoup(html, "html5lib")
        selector = "#highlight_D_A > table > tbody > tr:nth-child(2) > td:nth-child(4)"
        tags = soup.select(selector)
        equity = tags[0].text
        equity = equity.replace(",", "")
        equity = float(equity) * 100000000
        return equity
    except:
        return 

# 유통주식수
def get_shares(code):
    try:
        url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode={code}"
        resp = requests.get(url)
        html = resp.text 
        selector = "#svdMainGrid1 > table > tbody > tr:nth-child(7) > td:nth-child(2)"
        soup = BeautifulSoup(html, "html5lib")
        tags = soup.select(selector)
        shares = tags[0].text.split('/')[0]
        shares = shares.replace(',', '')
        shares = float(shares)
    except:
        shares = 0

    try:
        selector = "#svdMainGrid5 > table > tbody > tr:nth-child(5) > td:nth-child(3)"
        tags = soup.select(selector)
        self_shares = tags[0].text
        self_shares = self_shares.replace(',', '') 
        self_shares = float(self_shares)
    except:
        self_shares = 0

    return shares - self_shares

# 종목코드 
def get_code_list():
    url = "http://comp.fnguide.com/SVO2/common/lookup_data.asp?mkt_gb=1&comp_gb=1"
    resp = requests.get(url)
    data = resp.json()
    return data

if __name__ == "__main__":
    op = get_operating_profit("A005930")
    print(op)