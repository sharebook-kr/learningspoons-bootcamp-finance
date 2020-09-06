import requests
from bs4 import BeautifulSoup

def get_report_info(시작일, 기업코드):
    api_key = "a61de3bdebbc6a830abdeea61a407717e958072a"
    url = f"https://opendart.fss.or.kr/api/list.json"

    params = {
        "crtfc_key": api_key,
        "corp_code": 기업코드,
        "pblntf_ty": "A",
        "bgn_de": 시작일,
        "corp_cls": "Y",
        "page_no":1,
        "page_count":10
    }

    resp = requests.get(url, params=params)
    data = resp.json()

    for item in data['list']:
        url = f"http://m.dart.fss.or.kr/html_mdart/MD1007.html?rcpNo={item['rcept_no']}"
        print(url)


def get_dcmno_and_eleid(rcpNo):
    url = f"http://m.dart.fss.or.kr/viewer/main.st?rcpNo={rcpNo}&dcmNo=&_=1590949633152"
    resp = requests.get(url)
    data = resp.json()

    for item in data['toc'] :
        if "재무에 관한 사항" in item['tocText']:
            for sub_item in item['children']:
                if "요약재무정보" in sub_item['tocText']:
                    return (sub_item['dcmNo'], sub_item['eleId'])
    return None

def 유동자산(rcept_no):
    result = get_dcmno_and_eleid(rcept_no)
    if result == None:
        print("error")

    url = "http://m.dart.fss.or.kr/report/main.do"
    data = {
        "rcpNo": rcept_no,
        "dcmNo": result[0],
        "eleId": result[1]
    }

    resp = requests.post(url, data=data)
    soup = BeautifulSoup(resp.text, 'html5lib')
    sel = "tr:nth-child(2) > td:nth-child(2)"
    result = soup.select(sel)
    print(result[0].text)



get_report_info("20000101", "00164779")
# 유동자산("20200330004441")
# 14,457,602
