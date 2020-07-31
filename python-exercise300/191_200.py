# 191
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
#
# for day in data:
#     for price in day:
#         print(price + (price * 0.014 * 0.01))

# 192
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
#
# for day in data:
#     for price in day:
#         print(price + (price * 0.014 * 0.01))
#     print("----")

# 193
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
#
# result = []     # 비어있는 리스트 생성
# for day in data:
#     for price in day:
#         result.append(price + (price * 0.014 * 0.01))
# print(result)

# 194
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
#
# result = []
# for day in data:
#     day_price = []
#
#     for price in day:
#         new_price = price + (price *  0.014 * 0.01)
#         day_price.append(new_price)
#
#     # [2000.28, 3050.427, ....]
#     result.append(day_price)
#
# print(result)

# 195
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# # 100
# # 190
# # 310
# for day_price in ohlc[1:]:
#     print(day_price[3])

# 196
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for day_price in ohlc[1:]:
#     close = day_price[3]        # 각 거래일의 종가
#     if close > 150:             # 종가가 150 보다 크면
#         print(close)

# 197
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for day_price in ohlc[1:]:
#     open = day_price[0]
#     close = day_price[3]
#     if close >= open:
#         print(close)

# 198
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# # 변동폭: 고가 - 저가
#
# volatility =[]
# for day_price in ohlc[1:]:
#     high = day_price[1]
#     low = day_price[2]
#     diff = high-low
#     volatility.append(diff)
#
# print(volatility)

# 199
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# # 종가 > 시가, 변동성(고가-저가)
# for day_price in ohlc[1:]:
#     open, high, low, close = day_price
#     if close > open:
#         print(high-low)

# 200
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# # 각 거래일 수익금: 시가 - 종가
# # 총 수익금
# total_profit = 0
#
# for day_price in ohlc[1:]:
#     profit = day_price[0] - day_price[3]
#     total_profit += profit
#
# print(total_profit)
