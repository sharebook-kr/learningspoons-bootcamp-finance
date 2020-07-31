from kiwoom import *
import time

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

codes = kiwoom.GetCodeListByMarket('0') + kiwoom.GetCodeListByMarket('10')

for code in codes[:50]:            # 50 종목만
    kiwoom.SetInputValue("종목코드", code)
    kiwoom.CommRqData("opt10001", "opt10001", 0, "0101")

    per = kiwoom.tr_data['PER']
    print(code, per)
    time.sleep(0.2)
