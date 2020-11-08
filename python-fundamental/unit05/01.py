import pandas as pd
from pykrx import stock

# 종가 추가하기 
df1 =pd.read_excel("s-rim-all.xlsx", index_col=0, usecols=["cd", "nm", "gb", "자기자본", "ROE", "유통주식수"])
df2 = stock.get_market_ohlcv_by_ticker("20200420")
종가 = df2["종가"]
종가.index = 'A' + 종가.index 
df1['종가'] = 종가 

# 현재가 추가하기 
df3 = stock.get_market_ohlcv_by_ticker("20201106")
현재가 = df3['종가']
현재가.index = 'A' + 현재가.index
df1['현재가'] = 현재가 

# 요구수익률 필터링
K = 7.89
조건 = df1['ROE'] >= K
df = df1[조건].copy()
df["초과이익"] = df["자기자본"] * (df["ROE"] - K) * 0.01

# 기업가치 
W = 1.0
df["기업가치0"] = df["자기자본"] + df["초과이익"] * (W / (1 + K * 0.01 - W))
W = 0.9
df["기업가치1"] = df["자기자본"] + df["초과이익"] * (W / (1 + K * 0.01 - W))
W = 0.8
df["기업가치2"] = df["자기자본"] + df["초과이익"] * (W / (1 + K * 0.01 - W))
W = 0.7
df["기업가치3"] = df["자기자본"] + df["초과이익"] * (W / (1 + K * 0.01 - W))
W = 0.6
df["기업가치4"] = df["자기자본"] + df["초과이익"] * (W / (1 + K * 0.01 - W))
W = 0.5
df["기업가치5"] = df["자기자본"] + df["초과이익"] * (W / (1 + K * 0.01 - W))

# 적정주가 
df['주가0'] = df["기업가치0"] / df["유통주식수"]
df['주가1'] = df["기업가치1"] / df["유통주식수"]
df['주가2'] = df["기업가치2"] / df["유통주식수"]
df['주가3'] = df["기업가치3"] / df["유통주식수"]
df['주가4'] = df["기업가치4"] / df["유통주식수"]
df['주가5'] = df["기업가치5"] / df["유통주식수"]

# 종목 선정 
조건1 = df["종가"] <= df["주가3"]
조건2 = df['gb'] == "유가증권시장"
df_buy = df[조건1 & 조건2].copy()

df_buy["수익률"] = df_buy["현재가"] / df_buy["종가"] - 1
mean = df_buy["수익률"].mean()
print(mean)
print(df_buy.shape)
