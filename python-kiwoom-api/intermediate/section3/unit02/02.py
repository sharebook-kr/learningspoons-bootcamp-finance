from pykiwoom.kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("blocking login")

group = kiwoom.GetThemeGroupList(type=1)
print(type(group))
pprint.pprint(group)

#theme_id = group['타이어']
