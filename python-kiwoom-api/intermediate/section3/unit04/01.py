from pykiwoom.kiwoom import *

kiwoom = Kiwoom(login=True)    # 객체 생성 및 로그인

df = kiwoom.block_request("opt10001",
                          종목코드="005930",
                          output="주식기본정보",
                          next=0)

df.to_excel("주식기본정보.xlsx")
