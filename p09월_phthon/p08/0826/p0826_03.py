# num1 = 100
# num2 = 100
# num3 = 100
# print(num1, num2, num3)

# num4=num5=num6=1
# print(num4,num5,num6)

# # a1=1, a2="안녕" # 한 줄에 여러 변수에 여러개 값을 넣는 것은 불가
# # a=1, a1=2 # 에러
# a1 = 1
# a2 = "안녕"
# print(a1,a2)


# no1 = 100 # 변수선언과 동시에 값 전달
# print(10==10) # 같다 표현은 ==를 사용 True 가 나옴


# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b) # 10*10*10 / 10에 3제곱

# print : 출력
# input : 입력
# num = input("숫자를 입력하세요.")
# print("입력숫자 : {}".format(num))


# input으로 받은 모든 것은 문자열 타입이 된다.
# a = int(input("1번째 숫자를 입력하세요.")) # str 타입을 int타입으로 변경5
# b = int(input("2번째 숫자를 입력하세요."))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b) # 10*10*10 / 10에 3제곱


# 아이디/패스워드를 입력받아 출력하시오.
# 아이디 : aaa  패스워드 : 1111
id = input("아이디를 입력하세요. :")
pw = input("패스워드를 입력하세요. :")
print("아이디확인 : {}".format("aaa"==id))  #True, False
print("패스워드 확인 : {}".format("1111"==pw)) #True, False
print("아이디:{}, 패스워드:{}".format(id,pw))
