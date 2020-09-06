from selenium import webdriver

# 같은 경로에 chromedriver.exe가 위치해야 함
driver = webdriver.Chrome('chromedriver.exe')

ticker = "066570"
url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{ticker}&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=701"
driver.get(url)

ticker = "000660"
url = f"http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A{ticker}&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=701"
driver.get(url)