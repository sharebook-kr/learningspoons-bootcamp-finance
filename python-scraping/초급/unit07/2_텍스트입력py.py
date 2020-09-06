from selenium import webdriver

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naver.com')

selector = "#query"
ui = driver.find_element_by_css_selector(selector)
ui.send_keys("러닝스푼즈")

selector = "#search_btn"
ui = driver.find_element_by_css_selector(selector)
ui.click()
