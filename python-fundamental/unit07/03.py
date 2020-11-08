import requests
import pprint
import requests
import re 
import pandas as pd


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


if __name__ == "__main__":
    bs = get_balance_sheet("005930")
    print(bs.head())