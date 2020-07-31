# 201
#def print_coin():
#    print("비트코인")

# 202
#print_coin()

# 203
# for i in range(100):
#     print_coin()

# 204
# def print_coins():
#     for i in range(100):
#         print("비트코인")

# 205
# hello()
# def hello():
#     print("Hi")

# 206
# def message() :
#     print("A")
#     print("B")
#
# message()
# print("C")
# message()

# 207
# print("A")
#
# def message() :
#     print("B")
#
# print("C")
# message()

# 208
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()

# 209
# def message1():
#     print("A")
#
# def message2():
#     print("B")
#     message1()
#
# message2()

# 210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
