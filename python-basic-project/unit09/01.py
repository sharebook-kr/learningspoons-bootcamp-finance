import random

f = open("python-basic-project/unit09/data.txt")
lines = f.readlines()
f.close()

random.shuffle(lines)
for line in lines:
    print(line.strip())
