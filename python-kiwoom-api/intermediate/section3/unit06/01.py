from pykiwoom.kiwoom import *

kiwoom = Kiwoom(login=True)

account_list = kiwoom.GetLoginInfo("ACCNO")
account = account_list[0]

# opw00001
df = kiwoom.block_request("opw00001",
                          계좌번호=account,
                          비밀번호="",
                          비밀번호입력매체구분="00",
                          조회구분=1,
                          output="예수금상세현황",
                          next=0)

print(df)
df.to_excel("result.xlsx")
주문가능금액 = int(df['주문가능금액'][0])
print(주문가능금액)
