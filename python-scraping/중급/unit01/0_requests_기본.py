import requests

url = "https://finance.naver.com"
resp = requests.get(url)

print( resp.text )
# 네이버 금융 페이지의 기사에 따라 출력되는 결과가 강의와 다를 수 있음
print( "유럽증시" in resp.text )