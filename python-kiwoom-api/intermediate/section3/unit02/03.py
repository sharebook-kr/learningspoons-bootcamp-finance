from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("blocking login")

group = kiwoom.GetThemeGroupList(type=0)   # '141': XXX
print(group['141'])     # 딕셔너리에서 '141' 인덱싱

tickers = kiwoom.GetThemeGroupCode('141')
print(tickers)

for code in tickers:
    name = kiwoom.GetMasterCodeName(code)
    print(code, name)
