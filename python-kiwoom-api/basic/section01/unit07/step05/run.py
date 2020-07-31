from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

state = kiwoom.GetMasterStockState('005930')
print(state)

