from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

codes = kiwoom.GetCodeListByMarket('0') + kiwoom.GetCodeListByMarket('10')

for code in codes:
    date = kiwoom.GetMasterListedStockDate(code)
    name = kiwoom.GetMasterCodeName(code)
    if date.startswith('2020'):
        print(date, code, name)

