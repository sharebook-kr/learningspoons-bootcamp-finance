import os 

login_info = "C:/OpenAPI/system/Autologin.dat"
if os.path.isfile(login_info):
    os.rename("C:/OpenAPI/system/Autologin.dat", "C:/OpenAPI/system/Autologin.dat0")