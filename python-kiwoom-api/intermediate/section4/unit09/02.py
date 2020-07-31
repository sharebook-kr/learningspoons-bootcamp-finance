from pykiwoom.kiwoom import *
import datetime
import time

# 객체생성 및 로그인
kiwoom = Kiwoom(login=True)

# 전종목 종목코드
kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
codes = kospi + kosdaq

# 오늘날짜
now = datetime.datetime.now()
today = now.strftime("%Y%m%d")           # 날짜 타입 -> 문자열
#print(today)

for i, code in enumerate(codes):          # (0, "000020"), (1, "000040") ..
    print(i, len(codes))                  # 0, 2968

    df = kiwoom.block_request("opt10081",
                              종목코드=code,
                              기준일자=today,
                              수정주가구분=1,
                              output="주식일봉차트조회",
                              next=0)

    out_name = f"{code}.xlsx"      # "000020.xlsx"
    #out_name = "{}.xlsx".format(code)

    df.to_excel(out_name)
    time.sleep(3.6)
