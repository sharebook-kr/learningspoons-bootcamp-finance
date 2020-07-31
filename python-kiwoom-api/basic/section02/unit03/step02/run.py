from kiwoom import *
import time

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

# 첫 번째 조회
kiwoom.SetInputValue("종목코드", "005930")
kiwoom.SetInputValue("기준일자", "20200504")
kiwoom.SetInputValue("수정주가구분", 1)
kiwoom.CommRqData("opt10081", "opt10081", 0, "0101")

# 데이터가 남아 있다면 연속 조회
while kiwoom.remained:
    kiwoom.SetInputValue("종목코드", "005930")
    kiwoom.SetInputValue("기준일자", "20200504")
    kiwoom.SetInputValue("수정주가구분", 1)
    kiwoom.CommRqData("opt10081", "opt10081", 2, "0101")        # 연속조회
    time.sleep(3.6)