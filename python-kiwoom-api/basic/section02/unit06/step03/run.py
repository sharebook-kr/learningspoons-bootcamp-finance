from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

kiwoom.GetConditionLoad()
condition = kiwoom.GetConditionNameList()
print(condition)

# 조건식 인덱스에서 '000' 이나 0이나 둘 다 동작함
kiwoom.SendCondition("0101", "perpbr", 0, 0)
print(kiwoom.condition_codes)
