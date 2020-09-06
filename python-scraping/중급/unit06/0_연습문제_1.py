import requests

url = "https://shoppinghow.kakao.com/siso/p/api/hotdeal/list"
params = {
    "contentseq": "",
    "_": "1590304384521"
}
resp = requests.get(url, params=params)
result = resp.json()

for data in result['todayList']:
    print(f"{data['title']} / 최저가 {data['minPrice']}")

for data in result['hotdealList']:
    print(f"{data['title']} / 최저가 {data['minPrice']}")