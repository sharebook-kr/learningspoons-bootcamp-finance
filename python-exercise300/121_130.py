# 121
# data = input("문자입력: ")
# if data.islower():
#     print(data.upper())
# else:
#     print(data.lower())

# 122
# score = input("score: ")
# score = int(score)
# if score > 80:
#     print("grade is A")
# elif 60 < score <= 80:
#     print("grade is B")
# elif 40 < score <= 60:
#     print("grade is C")
# elif 20 < score <= 40:
#     print("grade is D")
# else:
#     print("grade is E")

# 123
# data = input("입력: ")   # 100 달러
# tokens = data.split()    # ['100', '달러']
# amount, currency = tokens
# amount = float(amount)
#
# if currency == '달러':
#     print(amount * 1167)
# elif currency == '엔':
#     print(amount * 1.096)
# elif currency == '유로':
#     print(amount * 1268)
# else:
#     print(amount * 171)

# 124
# num1 = int(input("input number1: "))
# num2 = int(input("input number2: "))
# num3 = int(input("input number3: "))
#
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)

# 125
# number = input("휴대전화 번호 입력: ")
# data = number[:3]
#
# if data == '011':
#     comp = "SKT"
# elif data == "016":
#     comp = "KT"
# elif data == "019":
#     comp = "LGU"
# else:
#     comp = "알수없음"
#
# print(f"당신은 {comp} 사용자입니다.")

# 126
# data = input("우편번호: ")
# data = data[:3]
# if data in ["010", "011", "012"]:
#     print("강북구")
# elif data in ["013", "014", "015"]:
#     print("도봉구")
# elif data in ["016","017", "018", "019"]:
#     print("노원구")
# else:
#     print("알수없음")

# 127
# data = input("주민등록번호: ")  # 111111-1234567
# tokens = data.split("-")        # ['111111', '1234567']
# data2 = tokens[1]
# if data2[0] == '1' or data2[0] == '3':
#     print("남자")
# elif data2[0] == '2' or data2[0] == '4':
#     print("여자")
# else:
#     print("알수없음")

# 128
# data = input("주민등록번호: ")  # 111111-1234567
# back = data.split("-")[1]
# if back[1:3] in ['00', '01', '02', '03', '04', '05', '06', '07', '08']:
#     print("서울 입니다. ")
# else:
#     print("서울이 아닙니다.")

# 129
# data = input("주민등록번호: ")
# data = data.replace("-", "")  # 8210101635210
#
# 계산1 = int(data[0]) * 2 + int(data[1]) * 3 + int(data[2]) * 4 + \
#        int(data[3]) * 5 + int(data[4]) * 6 + int(data[5]) * 7 + \
#        int(data[6]) * 8 + int(data[7]) * 9 + int(data[8]) * 2 + \
#        int(data[9]) * 3 + int(data[10]) * 4 + int(data[11]) * 5
#
# 계산1 = 계산1 % 11
# print(계산1)
#
# 계산2 = 11 - 계산1     # 0 ~ 10
# print(계산2)
#
# 계산2 = str(계산2)     # 0 -> '0' , 1 -> '1' , 10 -> '10'
# print(계산2)
#
# if data[-1] == 계산2[-1]:
#     print("유효한 주민등록번호입니다")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

# 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#
# open = float(btc['opening_price'])
# high = float(btc['max_price'])
# low = float(btc['min_price'])
# diff = high - low        # 변동폭
#
# if (open+diff) > high:
#     print("상승장")
# else:
#     print("하락장")




