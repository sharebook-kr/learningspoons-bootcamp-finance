from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

accounts = kiwoom.GetLoginInfo("ACCNO")
account = accounts.split(';')[0]
print(account)
kiwoom.SendOrder("매수", "0101", account, 1, "005930", 10, 0, "03", "")  # 시장가
#kiwoom.SendOrder("매수", "0101", account, 1, "005930", 1, 45000, "00", "")   # 지정가
#kiwoom.SendOrder("매수", "0101", account, 1, "005930", 1, 45001, "00", "")   # 지정가
#kiwoom.SendOrder("매수", "0101", account, 1, "005930", 1, 45001, "00", "")   # 지정가
#kiwoom.SendOrder("매수", "0101", account, 1, "094360", 1, 8100, "00", "")   # 지정가
#kiwoom.SendOrder("매수", "0101", account, 1, "094360", 1, 8090, "00", "")   # 지정가
#kiwoom.SendOrder("매수", "0101", account, 1, "094360", 1, 8091, "00", "")   # 지정가
#kiwoom.SendOrder("매수", "0101", account, 1, "000020", 10, 0, "03", "")  # 시장가
#kiwoom.SendOrder("매도", "0101", account, 2, "000020", 7, 0, "03", "")  # 시장가 매도
