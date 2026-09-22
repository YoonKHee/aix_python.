def cal(num1,num2,str):
    result = 0
    if str=="+":
        result = num1+num2
    elif str=="-":
        result = num1-num2
    elif str=="*":
        result = num1*num2
    elif str=="/":
        result = num1/num2
    return result


num1 = int(input("숫자입력"))
num2 = int(input("숫자입력"))
str = input("+,-,*,/ 중 하나 입력:")
result = cal(num1,num2,str)
print("결과값:",result)

# def add(num1,num2):
#     sum = num1+num2
#     return sum # 포출하는 곳으로 값 전달
# # 함수리턴
# while True:
#     num1 = int(input("숫자입력1:"))
#     num2 = int(input("숫자입력2:"))
#     total = add(num1,num2)
#     print("결과값:",total)




# 함수는 호출하는 명령어 위에 있어야 함.
# 함수의 매개변수 개수가 틀리면 에러

# def print1(num1,str1):
#     for i in range(num1):
#         print(i+1,str1)

# while True:
#     num1 = int(input("숫자입력:"))
#     str1 = input("출력하는 문구:")
#     print1(num1,str1)