data = [('kim', 9), ('lee', 5), ('park', 10)]

# lambda 사용
result = sorted(data, key=lambda x:x[1])
print(result)

# 함수 사용
def get_score(t):
    return t[1]

result1 = sorted(data, key=get_score)
print(result1)
