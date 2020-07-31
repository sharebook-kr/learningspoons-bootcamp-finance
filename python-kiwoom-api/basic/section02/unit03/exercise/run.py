from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

kiwoom.SetInputValue("종목코드", "005930")
kiwoom.SetInputValue("기준일자", "20200504")
kiwoom.SetInputValue("수정주가구분", 1)
kiwoom.CommRqData("opt10081", "opt10081", 0, "0101")
#print(kiwoom.tr_data)

kiwoom.tr_data.to_excel("삼성전자일봉.xlsx")