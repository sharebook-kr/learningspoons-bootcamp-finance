from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

cnt = kiwoom.GetMasterListedStockCnt('005935')
print(cnt, type(cnt))

