from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

# TR 사용하기
kiwoom.SetInputValue("종목코드", "005930")
kiwoom.CommRqData("opt10001", "opt10001", 0, "0101")   # 화면번호 "0000"은 제외
print(kiwoom.tr_data)