from selenium import webdriver
import time

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')

for ticker in ["005930", "066575", "000660"]:
    driver.get(f'https://finance.naver.com/item/main.nhn?code={ticker}')

    selector = "#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em"
    ui = driver.find_element_by_css_selector(selector)
    print(ui.text)

    time.sleep(2)
