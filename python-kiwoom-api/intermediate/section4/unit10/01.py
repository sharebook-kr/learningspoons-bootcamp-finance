import pandas as pd

df = pd.read_excel("000020.xlsx")
df2 = df[['현재가', '일자']].copy()

# 컬럼 이름 변경
df2.rename(columns={"현재가": "000020"}, inplace=True)
df2 = df2.set_index("일자")
df2 = df2[::-1]
print(df2)
