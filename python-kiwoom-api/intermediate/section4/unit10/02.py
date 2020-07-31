import os
import pandas as pd

flist = os.listdir()
xlsx_list = [x for x in flist if x.endswith(".xlsx")]

# xlsx_list = []
# for x in flist:
#     if x.endswith(".xlsx")
#         xlsx_list.append(x)

close_data = []
for xls in xlsx_list:
    code = xls[:6]              # xls -> "000020.xlsx"

    df = pd.read_excel(xls)
    df2 = df[['현재가', '일자']].copy()
    df2.rename(columns={"현재가": code}, inplace=True)
    df2 = df2.set_index("일자")
    df2 = df2[::-1]

    # 한 종목에 대한 데이터
    close_data.append(df2)          # DataFrame 객체를 리스트에 저장

# concat
df = pd.concat(close_data, axis=1)
df.to_excel("merge.xlsx")