from selenium import webdriver

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')

ticker = "005930"
url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{ticker}&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=701"
driver.get(url)

sel = "#bizSummaryHeader"
ui = driver.find_element_by_css_selector(sel)
print(ticker, ui.text)