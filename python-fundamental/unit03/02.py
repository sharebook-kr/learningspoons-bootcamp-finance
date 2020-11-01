import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# 자기자본 
def get_equity(code):
    try:
        # download html
        url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode={code}"
        resp = requests.get(url)
        html = resp.text 

        # scarping by css selector
        soup = BeautifulSoup(html, "html5lib")
        tags = soup.select("#highlight_D_A > table > tbody > tr:nth-child(10) > td:nth-child(4)")
        equity = tags[0].text
        equity = equity.replace(",", "")
        equity = float(equity) * 100000000
        return equity
    except:
        return 0

# ROE
def get_roe(code):
    try:
        url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode={code}"
        resp = requests.get(url)
        html = resp.text 
        soup = BeautifulSoup(html, "html5lib")
        tags = soup.select("#highlight_D_A > table > tbody > tr:nth-child(18) > td")
        
        roe1 = float(tags[0].text)
        roe2 = float(tags[1].text)
        roe3 = float(tags[2].text)

        if roe3 >= roe2 >= roe1 or roe3 <= roe2 <= roe1:
            roe = roe3
        else:
            roe  = (3 * roe3 + 2 * roe2 + 1 * roe1) / 6
        return roe
    except:
        return 0


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


def get_code_list():
    url = "http://comp.fnguide.com/SVO2/common/lookup_data.asp?mkt_gb=1&comp_gb=1"
    resp = requests.get(url)
    data = resp.json()
    return data


if __name__ == "__main__":
    code_list = get_code_list()

    for i, comp in enumerate(code_list):
        acode = comp['cd']
        name = comp['nm']
        자기자본 = get_equity(acode)
        ROE = get_roe(acode)
        유통주식수 = get_shares(acode)
        
        print(acode, name, 자기자본, ROE, 유통주식수)

        comp['자기자본'] = 자기자본
        comp['ROE'] = ROE
        comp['유통주식수'] = 유통주식수 

        time.sleep(0.1)
        print(i, "/", len(code_list))
    
    # dataframe
    df = pd.DataFrame(data=code_list)
    df.to_excel("data.xlsx")
    
