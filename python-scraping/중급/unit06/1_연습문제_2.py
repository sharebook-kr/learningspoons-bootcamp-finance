import requests

def 번역하기(string):
    url = "https://translate.kakao.com/translator/translate.json"
    headers = {
        "Referer": "https://translate.kakao.com/",
        "User-Agent": "Hello"
    }

    data = {
        "queryLanguage": "auto",
        "resultLanguage": "en",
        "q": string
    }

    resp = requests.post(url, headers=headers, data=data)
    result = resp.json()

    return result['result']['output'][0][0]

result = 번역하기("사랑합니다")
print(result)

result = 번역하기("인생은 짧다.")
print(result)