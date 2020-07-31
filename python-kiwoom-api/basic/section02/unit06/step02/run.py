from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

kiwoom.GetConditionLoad()
condition = kiwoom.GetConditionNameList()
print(condition)

