from selenium import webdriver
import time

def get_business_summary(driver, ticker):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{ticker}&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=701"
    driver.get(url)

    sel = "#bizSummaryHeader"
    ui = driver.find_element_by_css_selector(sel)
    return ui.text

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')

file = open("out.txt", "w")

for ticker in ["005930", "000660", "006800", "072870"]:
    summary = get_business_summary(driver, ticker)
    file.write(f"{ticker} {summary}" + "\n")
    time.sleep(1)

file.close()