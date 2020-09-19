import random 

com = random.choice(["가위", "바위", "보"])
print(com)

user = input("입력: ")
print(user)

# 결과 판단 
winner = None
if com == "가위":
    if user == "가위":
        winner = None
    elif user == "바위":
        winner = "user"
    else:
        winner = "computer"
elif com == "바위":
    if user == "가위":
        winner = "computer"
    elif user == "바위":
        winner = None
    else:
        winner = "user"
else:
    if user == "가위":
        winner = "user"
    elif user == "바위":
        winner = "computer" 
    else:
        winner = None 

if winner == "computer":
    print("컴퓨터: ", com)
    print("사용자: ", user)
    print("승자 : ", "컴퓨터")
elif winner == "user":
    print("컴퓨터: ", com)
    print("사용자: ", user)
    print("승자 : ", "사용자")
else:
    print("컴퓨터: ", com)
    print("사용자: ", user)
    print("승자 : ", "무승부")








