from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

date = kiwoom.GetMasterListedStockDate('005930')
print(date, type(date))

