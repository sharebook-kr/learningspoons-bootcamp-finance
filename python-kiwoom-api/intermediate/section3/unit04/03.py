from pykiwoom.kiwoom import *
import time

kiwoom = Kiwoom(login=True)

df = kiwoom.block_request("opt10081",
                          종목코드="005930",
                          기준일자="20200628",
                          수정주가구분=1,
                          output="주식일봉차트조회",
                          next=0)
print(df.head())
time.sleep(3.6)

while kiwoom.tr_remained:
    df = kiwoom.block_request("opt10081",
                              종목코드="005930",
                              기준일자="20200628",
                              수정주가구분=1,
                              output="주식일봉차트조회",
                              next=2)
    time.sleep(3.6)
    print(df.head())