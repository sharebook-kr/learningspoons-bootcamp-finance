import requests

url = "https://api.upbit.com/v1/market/all"
params = {
    "isDetails":"false"
}

resp = requests.get(url, params=params)
data = resp.json()
print(data)
