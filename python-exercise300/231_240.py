#231
# def n_plus_1 (n):
#     result = n + 1
#
# n_plus_1(3)
# print (result)

# 232
#make_url("naver")
#www.naver.com
# def make_url(name):
#     domain = "www." + name + ".com"
#     return domain
#
# result = make_url("naver")
# print(result)

# 233
# def make_list(mystr):
#     data = []
#     for i in mystr:
#         data.append(i)   # i->'a'
#
#     return data
#
# a = make_list("abcd")
# print(a)

# 234
# def pickup_even(nums):
#     even = []
#     for i in nums:       # nums 안에 있는 각각을 i로 바인딩할 때
#         if i % 2 == 0:  # i가 짝수면
#             even.append(i)
#     # 반복끝
#     return even
#
# ret = pickup_even([3, 4, 5, 6, 7, 8])
# print(ret)

# 235
# def convert_int(mystr):
#     mystr1 = mystr.replace(',', '')
#     return int(mystr1)
#
# a = convert_int("1,234,567")
# print(a)

# 236
# def 함수(num) :
#     return num + 4
#
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# 237
# def 함수(num) :
#     return num + 4
#
# c = 함수(함수(함수(10)))
# print(c)

# 238
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     return num * 10
#
# a = 함수1(10)
# c = 함수2(a)
# print(c)

# 239
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
#
# c = 함수2(10)
# print(c)

# 240
# def 함수0(num) :
#     return num * 2
#
# def 함수1(num) :
#     return 함수0(num + 2)
#
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
#
# c = 함수2(2)
# print(c)