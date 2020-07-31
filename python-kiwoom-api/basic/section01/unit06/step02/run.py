from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

name = kiwoom.GetMasterCodeName('005930')
print(name)

