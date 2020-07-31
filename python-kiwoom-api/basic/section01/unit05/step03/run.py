from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

cnt = kiwoom.GetLoginInfo("ACCOUNT_CNT")
print(cnt)