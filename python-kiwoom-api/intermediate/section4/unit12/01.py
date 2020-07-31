import pandas as pd
from pykiwoom.kiwoom import *

df = pd.read_excel("momentum_list.xlsx")
df.columns = ["종목코드", "모멘텀", "순위"]
print(df)

# 종목명 컬럼 추가
kiwoom = Kiwoom(login=True)

codes = df["종목코드"]
names = []
for code in codes:
    name = kiwoom.GetMasterCodeName(code)
    names.append(name)

df["종목명"] = pd.Series(data=names)
print(df)