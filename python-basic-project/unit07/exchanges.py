import requests
from bs4 import BeautifulSoup


def get_usd():
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8"
    resp = requests.get(url)
    html = resp.text

    soup = BeautifulSoup(html, "html5lib") 
    selector = "#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr:nth-child(1) > td:nth-child(2) > span"
    tags = soup.select(selector)
    val = tags[0].text
    val = val.replace(",", "")
    return float(val)

def get_jpy():
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8"
    resp = requests.get(url)
    html = resp.text

    soup = BeautifulSoup(html, "html5lib") 
    selector = "#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr:nth-child(2) > td:nth-child(2) > span"
    tags = soup.select(selector)
    val = tags[0].text
    val = val.replace(",", "")
    return float(val)


def get_eur():
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8"
    resp = requests.get(url)
    html = resp.text

    soup = BeautifulSoup(html, "html5lib") 
    selector = "#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr:nth-child(3) > td:nth-child(2) > span"
    tags = soup.select(selector)
    val = tags[0].text
    val = val.replace(",", "")
    return float(val)


