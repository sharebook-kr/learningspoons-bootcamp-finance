import requests


def 종가조회(ticker, limit=10):
    url = f"https://finance.daum.net/api/charts/A{ticker}/days"
    params = {
        "limit": limit,
        "adjusted": "true"
    }

    headers = {
        "referer": f"https://finance.daum.net/chart/A{ticker}",
        "user-agent": "Mozilla/5.0"
    }
    resp = requests.get(url, headers=headers, params=params)
    result = resp.json()

    for item in result['data']:
        print(f"일자:{item['date']} / 종가:{item['tradePrice']}")


종가조회("000660", 5)