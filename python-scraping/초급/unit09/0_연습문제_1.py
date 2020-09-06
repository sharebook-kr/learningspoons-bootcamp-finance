from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://investing.com/indices/us-spx-500')

selector = "#leftColumn > div:nth-child(20) > article.js-article-item.articleItem > div.textDiv > a"
wait = WebDriverWait(driver, 3)
data = (By.CSS_SELECTOR, selector)
ui = wait.until(EC.presence_of_element_located( data ))
print(ui.text)