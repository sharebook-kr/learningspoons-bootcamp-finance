from selenium import webdriver

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naver.com')

selector = "#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(9) > a"
ui = driver.find_element_by_css_selector(selector)
ui.click()