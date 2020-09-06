import requests
import zipfile
import xmltodict

# 본인의 API-KEY로 변경하세요.
api_key = "a61de3bdebbc6a830abdeea61a407717e958072a"
url = "https://opendart.fss.or.kr/api/corpCode.xml"

params = {
    "crtfc_key": api_key
    }

resp = requests.get(url, params=params)
print(resp)

f = open('corp_code.zip', "wb")
f.write(resp.content)
f.close()

zf = zipfile.ZipFile('corp_code.zip')
zf.extractall()
zf.close()

f = open("CORPCODE.xml", encoding="utf-8")
data = f.read()
f.close()

result = xmltodict.parse(data)
for item in result['result']['list'][:5]:
    print(item['corp_name'], item['corp_code'])

