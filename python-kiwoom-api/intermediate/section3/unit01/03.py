from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

state = kiwoom.GetConnectState()
if state == 0:
    print("미 연결")
elif state == 1:
    print("연결완료")
else:
    print("unknown")



