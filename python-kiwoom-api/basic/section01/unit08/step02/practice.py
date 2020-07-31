from kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

data = kiwoom.GetThemeGroupList(0)
themes = list(data.keys())

for name in themes:
    if '태양광' in name:
        print(name, data[name])

