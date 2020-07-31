from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

theme = kiwoom.GetThemeGroupList(0)
codes = kiwoom.GetThemeGroupCode('100')

print("테마코드: {} 테마명: {}".format('100', theme['100']))
for code in codes:
    name = kiwoom.GetMasterCodeName(code[1:])
    print(code, name)
