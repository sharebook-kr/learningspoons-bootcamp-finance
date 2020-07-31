from pykiwoom.kiwoom import *

# 객체생성 및 로그인
kiwoom = Kiwoom(login=True)

# 전종목 종목코드
kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
codes = kospi + kosdaq
print(codes)
print(len(codes))
