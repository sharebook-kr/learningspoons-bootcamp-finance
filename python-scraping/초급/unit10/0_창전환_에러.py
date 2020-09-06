from selenium import webdriver

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://comp.fnguide.com/')

selector = "#svdMainChart11 > a"
ui = driver.find_element_by_css_selector(selector)
ui.click()

# 아래 코드는 에러!
# - 창전환이 필요
selector = "#chartDataGrid > table > tbody > tr.rwf > td:nth-child(2)"
driver.find_element_by_css_selector(selector)
print(ui.text)
