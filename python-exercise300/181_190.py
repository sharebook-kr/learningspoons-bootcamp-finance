# 181
# apart = [ ["101호", "102호"],
#           ["201호", "202호"],
#           ["301호", "302호"] ]

# 182
# stock = [["시가", 100, 200, 300],
#          ["종가", 80, 210, 330]]

# 183
# stock = {
#     "시가": [100, 200, 300],
#     "종가": [80, 210, 330]
# }

# 184
# stock = {
#     "10/10": [80, 110, 70, 90],
#     "10/11": [210, 230, 190, 200]
# }

# 185
# apart = [ [101, 102],
#           [201, 202],
#           [301, 302] ]
#
# for 층 in apart:
#     for 집 in 층:
#         print(집, "호")

# 186
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for 층 in apart[::-1]:
#     for 집 in 층:
#         print(집, "호")

# 187
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for 층 in apart[::-1]:
#     for 집 in 층[::-1]:
#         print(집, "호")

# 188
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for 층 in apart:
#     for 집 in 층:
#         print(집, "호")
#         print("-----")

# 189
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for 층 in apart:
#     for 집 in 층:
#         print(집, "호")
#     # 안쪽 for문의 끝나는 지점
#     print("-----")

# 190
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for 층 in apart:
#     for 집 in 층:
#         print(집, "호")
#     # 층의 끝
# # 아파트의 끝
# print("-----")