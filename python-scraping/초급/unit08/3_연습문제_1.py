from selenium import webdriver

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://finance.naver.com')

# 1) 반복문 사용
for i in range(1, 7):
    selector = f"#content > div.article > div.section > div.news_area > div > ul > li:nth-child({i}) > span > a"
    ui = driver.find_element_by_css_selector(selector)
    print(ui.text)

# 2) find_elements_by_css_selector 메서드 사용
selector = "#content > div.article > div.section > div.news_area > div > ul > li > span > a"
result = driver.find_elements_by_css_selector(selector)
for item in result:
    print(item.text)

