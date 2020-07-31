from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

kiwoom.SetInputValue("종목코드", "005930")
kiwoom.SetInputValue("기준일자", "20200517")
kiwoom.SetInputValue("수정주가구분", 1)
kiwoom.CommRqData("opt10081", "opt10081", 0, "0101")
