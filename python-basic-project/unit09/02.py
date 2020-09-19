import random
import time 

f = open("python-basic-project/unit09/data.txt")
lines = f.readlines()
f.close()

random.shuffle(lines)


for line in lines:
    line = line.strip()
    print(line)
    start = time.time()
    user = input("")
    end  = time.time()

    if line.strip() == user:
        elapsed = end - start 
        speed = (len(line) / elapsed) * 60
        print("타수: ", speed)
