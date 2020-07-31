# 251

# 252
# class Human:
#     pass

# 253
# class Human:
#     pass
#
# areum = Human()

# 254
# class Human:
#     def __init__(self):
#         print("응애응애")
#
# areum = Human()

# 255
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# areum = Human("아름", 25, "여자")
# print(areum.name)

# 256
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# areum = Human("아름", 25, "여자")
# print(areum.age)

# 257
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def who(self):
#         print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
#
# areum = Human("아름", 25, "여자")
# areum.who()      # Human.who(areum)

# 258
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def who(self):
#         print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
#
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#
# areum = Human("불명", "미상", "모름")
# areum.who()      # Human.who(areum)
#
# areum.setInfo("아름", 25, "여자")
# areum.who()      # Human.who(areum)

# 259
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __del__(self):
#         print("나의 죽음을 알리지마라")
#
#     def who(self):
#         print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
#
#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# areum = Human("아름", 25, "여자")
# del(areum)

# 260
# class OMG :
#     def print() :
#         print("Oh my god")
#
#
# mystock = OMG()
# mystock.print()      # OMG.print(mystock)

