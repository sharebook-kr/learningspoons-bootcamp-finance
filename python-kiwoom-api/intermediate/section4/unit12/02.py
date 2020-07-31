import pandas as pd
from pykiwoom.kiwoom import *
import time

df = pd.read_excel("momentum_list.xlsx")
df.columns = ["종목코드", "모멘텀", "순위"]
codes = df["종목코드"]

kiwoom = Kiwoom(login=True)
accounts = kiwoom.GetLoginInfo("ACCNO")
account = accounts[0]

for code in codes:
    kiwoom.SendOrder("시장가매수", "0101", account, 1, code, 10, 0, "03", "")
    time.sleep(0.2)
    print(code, "종목 시장가 주문 완료")



