import requests
import pprint
import requests
import re 
import pandas as pd
from bs4 import BeautifulSoup
import time
import numpy as np
import random

UNIT1 = 100000000

# encparam
def get_encparam(code):
    url = f"https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={code}"
    resp = requests.get(url)
    text = resp.text
    encparam = re.search("encparam: '(.+)'", text)[1].strip()
    return encparam


# 네이버 금융 재무상태표 
def get_balance_sheet(code):
    try:
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
        df = pd.DataFrame(data)
        df.set_index('ACCODE', inplace=True)
        return df
    except:
        return None


# 영업이익
def get_operating_profit(acode):
    try:
        # download html
        url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode={acode}"
        resp = requests.get(url)
        html = resp.text 

        # scarping by css selector
        soup = BeautifulSoup(html, "html5lib")
        selector = "#highlight_D_A > table > tbody > tr:nth-child(2) > td:nth-child(4)"
        tags = soup.select(selector)
        equity = tags[0].text
        equity = equity.replace(",", "")
        equity = float(equity) * UNIT1 
        return equity
    except:
        return 0 

# 유통주식수
def get_shares(acode):
    try:
        url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode={acode}"
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

def get_유동자산(bs):
    try:
        유동자산 = bs.loc["112830", "DATA5"] * UNIT1
        return 유동자산 
    except:
        return np.nan

def get_유동부채(bs):
    try:
        유동부채 = bs.loc["131580", "DATA5"] * UNIT1
        return 유동부채 
    except:
        return np.nan

def get_투자자산(bs):
    try:
        투자자산 = bs.loc["190310", "DATA5"] * UNIT1
        return 투자자산 
    except:
        return np.nan

def get_비유동부채(bs):
    try:
        비유동부채 = bs.loc["130010", "DATA5"] * UNIT1
        return 비유동부채 
    except:
        return np.nan

if __name__ == "__main__":
    code_list = get_code_list()
    data_list = []

    for i, comp in enumerate(code_list):
        if i < 1900:
            continue
        acode = comp['cd']
        code = comp['cd'][1:]
        name = comp['nm']
        df = get_balance_sheet(code)

        사업가치 = get_operating_profit(acode) * 10
        유동자산 = get_유동자산(df)
        유동부채 = get_유동부채(df)
        투자자산 = get_투자자산(df)
        비유동부채 = get_비유동부채(df)

        data = {}
        data['종목코드'] = code 
        data['종목명'] = name 
        data['사업가치'] = 사업가치 
        try:
            data["재산가치"] = 유동자산 - (유동부채 * 1.2) + 투자자산
        except: 
            data["재산가치"] = np.nan 
        data["비유동부채"] = 비유동부채

        print(i, code, 유동자산, 유동부채, 투자자산, 비유동부채) 
        #interval = random.randint(20, 100)    # 2 ~ 10 sec
        interval = random.randint(1, 50)    # 2 ~ 10 sec
        time.sleep(interval * 0.1)   
        print(i, "/", len(code_list))
        data_list.append(data)

        # 50개 단위로 저장 
        if i % 50 == 49:
            df = pd.DataFrame(data=data_list)
            index = i + 1
            df.to_excel(f"smart_data_{index}.xlsx")
            data_list = []       # 리스트 비우기 
    
    # dataframe
    df = pd.DataFrame(data=data_list)
    df.to_excel("smart_data_last.xlsx")




    
