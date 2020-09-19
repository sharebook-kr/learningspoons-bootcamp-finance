import random 

num = random.randint(1, 4)
print(num)

user = input("입력: ")
user = int(user)
print(user)

if num == user:
    print("정답")
elif num > user:
    print("Up")
else:
    print("Down")