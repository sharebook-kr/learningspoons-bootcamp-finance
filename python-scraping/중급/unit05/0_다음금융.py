import requests

url = "https://finance.daum.net/api/sectors?market=KOSDAQ&change=RISE&includedStockLimit=1&perPage=5"
headers = {
    "referer": "https://finance.daum.net/",
    "user-agent": "Hello",
}
resp = requests.get(url, headers=headers)
result = resp.json()
print(result['data'][-1]['sectorName'])

for item in result['data']:
    print(item['sectorName'])