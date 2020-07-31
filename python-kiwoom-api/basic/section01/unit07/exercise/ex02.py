from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

codes = kiwoom.GetCodeListByMarket('0') + kiwoom.GetCodeListByMarket('10')

for code in codes:
    state = kiwoom.GetMasterStockState(code)
    tokens = state.split("|")

    tarket = False
    if '거래정지' in tokens:
        tarket = True
    elif '관리종목' in tokens:
        tarket = True
    elif '감리종목' in tokens:
        tarket = True
    elif '투자유의종목' in tokens:
        tarket = True

    if tarket:
        print(code, state)

