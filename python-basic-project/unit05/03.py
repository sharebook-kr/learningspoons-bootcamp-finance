import random 

num = random.randint(1, 100)
print(num)

while True:
    user = input("입력: ")
    user = int(user)
    print(user)

    if num == user:
        print("정답")
        break
    elif num > user:
        print("Up")
    else:
        print("Down")