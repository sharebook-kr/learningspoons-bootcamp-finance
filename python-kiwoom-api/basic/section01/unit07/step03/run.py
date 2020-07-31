from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

price = kiwoom.GetMasterLastPrice('005930')
print(price, type(price))

