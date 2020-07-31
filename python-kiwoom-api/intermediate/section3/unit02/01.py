from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect()
print("blocking login")

price = kiwoom.GetMasterLastPrice("005930")
print(price, type(price))