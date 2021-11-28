import requests

url = "https://api.korbit.co.kr/v1/ticker"
params = {"currency_pair": "btc_krw"}
resp = requests.get(url=url, params=params)
data = resp.json()
print(data)
