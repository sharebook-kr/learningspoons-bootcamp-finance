from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("blocking login")

kiwoom.GetConditionLoad()
print("blocking load")

conditions = kiwoom.GetConditionNameList()
condition = conditions[0]   # tuple
condition_index, condition_name = condition

codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

for code in codes:
    name = kiwoom.GetMasterCodeName(code)
    print(code, name)
