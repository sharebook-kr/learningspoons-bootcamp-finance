import myfinance
import time
import random

kospi = myfinance.get_tickers()
data = [] 

for i, code in enumerate(kospi):
    dvr = myfinance.get_dvr(code)
    data.append((code, dvr))

    time.sleep(0.2)
    print(i, len(kospi), code)

# 정렬하기 
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data[:10])

