# 241
# import datetime
#
# now = datetime.datetime.now()
# print(now)

# 242
# import datetime
#
# now = datetime.datetime.now()
# print(type(now))

# 243
# import datetime
#
# now = datetime.datetime.now()
#
# for i in range(-5, 0):
#     delta = datetime.timedelta(days=i)      # -5, -4, ..., -1
#     print(now + delta)

# 244
# import datetime
#
# now = datetime.datetime.now()
# a = now.strftime("%H:%M:%S")
# print(a, type(a))

# 245
# 문자열->시간타입
"2020-06-14"
# import datetime
#
# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))

# 246
# import time
# import datetime
#
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 247
#import os                   # os.rename()
#from os import rename       # rename()
#from os import *            # getcwd(), rename(), ....
#import os as myos           # myos.getcwd()

# 248
# import os
# ret = os.getcwd()
# print(ret, type(ret))

# 249
#import os
#os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

# 250
# import numpy
# for i in numpy.arange(0, 5, 0.1):
#     print(i)
