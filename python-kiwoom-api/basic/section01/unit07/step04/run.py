from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

data = kiwoom.GetMasterConstruction('005930')
print(data)

