from kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("로그인 완료")

data = kiwoom.GetThemeGroupCode('100')
print(data)

