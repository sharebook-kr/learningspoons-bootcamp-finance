# 221
# def print_reverse(mystr):
#     print(mystr[::-1])
#
# print_reverse("hello")
# print_reverse("python")

# 222
#def print_score(scores):  # python list
#    average = sum(scores) / len(scores)
#    print(average)
#
#print_score([1, 2, 3])

# 223
# def print_even(data):       # data -> python list
#     for i in data:
#         if i % 2 == 0:
#             print(i)
#
# print_even([1, 2, 3, 4])

# 224
# def print_keys(mydict):
#     keys = mydict.keys()
#     for k in keys:
#         print(k)
#
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
#
# def print_value_by_key(mydict, key):
#     print(mydict[key])
#
# print_value_by_key  (my_dict, "10/26")

# 226
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸
# def print_5xn(mystr):
#     times = len(mystr) / 5      # 0.6
#     times = int(times+0.9)      # 1.5->1
#
#     for i in range(times):              # i -> 0, 1
#         print(mystr[5*i: 5*i+5])       #[0:5], [5:10]
#
# print_5xn("아이엠어보이유알어걸추가")

# 227
#printmxn("아이엠어보이유알어걸", 3)
# import math
#
# def printmxn(data, num):
#     # 횟수를 계산
#     times = len(data) / num
#     times = math.ceil(times)
#
#     for i in range(times):
#         print(data[i*num: (i+1)*num])
#
#
# printmxn("아이엠어보이유알어걸", 3)

# 228
#calc_monthly_salary(12000000)
# def calc_monthly_salary(annual):
#     print(int(annual/12))
#
# calc_monthly_salary(12000100)

# 229
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(a=100, b=200)

# 230
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(b=100, a=200)