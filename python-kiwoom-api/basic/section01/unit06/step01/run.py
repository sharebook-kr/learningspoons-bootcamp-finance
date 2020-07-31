from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

codes = kiwoom.GetCodeListByMarket('0')
print(codes)

