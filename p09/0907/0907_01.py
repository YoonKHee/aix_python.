# def add():
#     sum = 0
#     num = int(input("숫자입력:"))
#     for i in range(1,num+1):
#         sum += i 
#     print(sum)

# def add2(num):
#     sum = 0
#     for i in range(1,num+1):
#         sum += i 
#     print(sum)
#     return num


# def add3(num2,num3):
#     sum = 0
#     for i in range(num2,num3+1):
#         sum += i
#     print(sum)

def add4(num5,num6):
    sum = 0
    for i in range(num5,num6+1):
        sum += i
    return sum

# for i in range(10):
#     num = int(input("숫자입력:"))
#     sum = 0
#     for i in range(1,num+1):
#         sum += i
#     print(sum)

# # 10번 반복
# for i in range(10):
#     add()

# 매개변수 1개
# for i in range(10):
#     num = int(input("숫자입력:"))
#     add2(num)


# # 매개변수 2개
# num2 = int(input("숫자입력"))
# num3 = int(input("숫자입력"))
# add3(num2,num3)

num5 = int(input("숫자입력"))
num6 = int(input("숫자입력"))
sum = add4(num5,num6)
print(sum)