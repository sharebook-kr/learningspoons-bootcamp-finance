from selenium import webdriver

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://finance.naver.com/item/main.nhn?code=005930')

selector = "#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em"
ui = driver.find_element_by_css_selector(selector)
print(ui.text)
