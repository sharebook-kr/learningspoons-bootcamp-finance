from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)   # 로그인이 될때까지 여기서 대기
print("블록킹 로그인 완료")

accounts = kiwoom.GetLoginInfo("ACCNO")
print(accounts)
