from kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

data = kiwoom.GetThemeGroupList(1)
pprint.pprint(data)

