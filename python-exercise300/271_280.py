# 271
# import random
#
# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#
# kim = Account("김민수", 100)
# print(kim.name)
# print(kim.balance)
# print(kim.bank)
# print(kim.account_number)

# 272
# import random
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#
#         Account.account_count += 1
#
#
# kim = Account("김민수", 100)
# print(Account.account_count)
# lee = Account("이민수", 100)
# print(Account.account_count)
#

# 273
# import random
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count +=1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)     # Account.account_count
#
#
# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# kim.get_account_num()

# 274
# import random
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count +=1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)     # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount

# 275
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
# k = Account("kim", 100)
# k.deposit(100)
# k.withdraw(90)
# print(k.balance)

# 276
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
#
# p = Account("파이썬", 10000)
# p.display_info()
#

# 277
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)
#
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
# p = Account("파이썬", 10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(5000)
# p.deposit(5000)
# print(p.balance)

# 278
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)
#
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
# data = []
# k = Account("KIM", 10000000)
# l = Account("LEE", 10000)
# p = Account("PARK", 10000)
#
# data.append(k)
# data.append(l)
# data.append(p)
#
# print(data)

# 279
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)
#
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
# data = []
# k = Account("KIM", 10000000)
# l = Account("LEE", 10000)
# p = Account("PARK", 10000)
# data.append(k)
# data.append(l)
# data.append(p)
#
# for c in data:
#     if c.balance >= 1000000:
#         c.display_info()

# 280
# import random
#
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#         self.deposit_log = []
#         self.withdraw_log = []
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1
#
#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count
#
#     def deposit(self, amount):
#         if amount >= 1:
#             self.deposit_log.append(amount)
#             self.balance += amount
#
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)
#
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.withdraw_log.append(amount)
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)
#
#     def withdraw_history(self):
#         for amount in self.withdraw_log:
#             print(amount)
#
#     def deposit_history(self):
#         for amount in self.deposit_log:
#             print(amount)
#
#
# k = Account("Kim", 1000)
# k.deposit(100)
# k.deposit(200)
# k.deposit(300)
# k.deposit_history()
#
# k.withdraw(100)
# k.withdraw(200)
# k.withdraw_history()
