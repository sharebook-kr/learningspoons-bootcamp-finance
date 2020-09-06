from selenium import webdriver
import time

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://comp.fnguide.com/')

selector = "body > div.fng_body > div > div.headwrap > div.headertop > div > form > div > a"
ui = driver.find_element_by_css_selector(selector)
ui.click()

# 새창으로 이동
driver.switch_to.window( driver.window_handles[-1])

selector = "#txtSearchKey"
ui = driver.find_element_by_css_selector(selector)
ui.send_keys("SK하이닉스")

selector = "#btnSearch"
ui = driver.find_element_by_css_selector(selector)
ui.click()

time.sleep(3)

selector = "#body_contents > tr > td.l"
ui = driver.find_element_by_css_selector(selector)
ui.click()
