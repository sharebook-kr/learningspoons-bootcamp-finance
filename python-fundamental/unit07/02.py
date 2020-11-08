# 네이버 금융 encparam
import requests
import re 

url = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=005930"
resp = requests.get(url)
text = resp.text
encparam = re.search("encparam: '(.+)'", text)[1].strip()
print(encparam)