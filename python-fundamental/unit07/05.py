import requests
import pprint
import requests
import re 
import pandas as pd
from bs4 import BeautifulSoup
import time


# encparam
def get_encparam(code):
    url = f"https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={code}"
    resp = requests.get(url)
    text = resp.text
    encparam = re.search("encparam: '(.+)'", text)[1].strip()
    return encparam


# 네이버 금융 재무상태표 
def get_balance_sheet(code):
    encparam = get_encparam(code)
    url = "https://navercomp.wisereport.co.kr/v2/company/cF3002.aspx"

    headers = {
        "Host": "navercomp.wisereport.co.kr", 
        "Referer": f"https://navercomp.wisereport.co.kr/v2/company/c1030001.aspx?cmp_cd={code}&cn=", 
        "User-Agent": "Mozilla/5.0"
    }

    params = {
        "cmp_cd": f"{code}",
        "frq": "0",
        "rpt": "1",
        "finGubun": "MAIN",
        "frqTyp": "0",
        "encparam": encparam
    }

    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()
    data = data['DATA']
    return pd.DataFrame(data)


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
    df = get_balance_sheet("005930")
    df['ACC_NM'] = df['ACC_NM'].str.replace('.', '')
    df.set_index('ACC_NM', inplace=True)
    df2 = df.loc[['유동자산', '투자자산', '유동부채', '비유동부채'], 'DATA5']
    df2.dropna(inplace=True)

    재산가치 = df2["유동자산"]-(df2["유동부채"] * 1.2) + df2["투자자산"]
    재산가치 = 재산가치 * 100000000

    # 비유동부채
    비유동부채 = df2["비유동부채"] * 100000000
    print("재산가치", 재산가치)
    print("비유동부채", 비유동부채)


    
