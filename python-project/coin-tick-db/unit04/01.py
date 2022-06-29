import datetime

now = datetime.datetime.strptime("2022-06-29 08:59:59", "%Y-%m-%d %H:%M:%S")
print(now)

delta = datetime.timedelta(hours=9)
print(now - delta)