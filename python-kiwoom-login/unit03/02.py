import os 

login_info = "C:/OpenAPI/system/Autologin.dat0"
if os.path.isfile(login_info):
    os.rename("C:/OpenAPI/system/Autologin.dat0", "C:/OpenAPI/system/Autologin.dat")