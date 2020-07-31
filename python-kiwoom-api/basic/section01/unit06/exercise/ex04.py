from kiwoom import *
from pandas import DataFrame

kiwoom = Kiwoom()
kiwoom.CommConnect()

kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
total = kospi + kosdaq

rows = []
for code in total:
    name = kiwoom.GetMasterCodeName(code)
    rows.append((code, name))

columns = ['code', 'name']
df = DataFrame(data=rows, columns=columns)
df = df.set_index('code')
df.to_excel("code.xlsx")
