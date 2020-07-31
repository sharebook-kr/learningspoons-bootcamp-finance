import requests

url = "https://api.upbit.com/v1/market/all"
params = {
    "isDetails":"false"
}

resp = requests.get(url, params=params)
data = resp.json()

krw_codes = []

for data in data:
    code = data["market"]
    if code.startswith("KRW"):
        krw_codes.append(code)

print(krw_codes)