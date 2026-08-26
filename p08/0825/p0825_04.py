# 변수는 어떠한 값을 저장하는 공간, 타입은 값을 입력할때 정해짐
# 총 4가지 타입이 있다. bool(참, 거짓), 정수, 실수, 문자열 타입


a = 10   # 숫자형타입 - 정수타입
b = 10.1 # 숫자형탑 - 실수타입, 소수점
aa = "안녕" # 문자열타입
abc = True # 불타입(bool) - True, False / Boolean

# True는 이미 변수타입이라 True를 새로운 변수로 지정해서 사용할수 없음
# 이미 변수가 정해진 함수들은 새로운 변수로 사용할 수 없다

#예약어는 변수로 사용 할 수 없음
# ex) True = 1, print = 5


# print(10+5)
# print(10-5)
# print(10*5)
# print(10/5)  
# print(10//5) # 몫 2
# print(10%5)  # 나머지 0
# print(10**5) # 제곱 100000

# a = 10
# b = 4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)  
# print(a//b) # 몫 2
# print(a%b)  # 나머지 0
# print(a**b) # 제곱 100000


# a = 10
# b = 4
# print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)

# 타입확인
a = 100
b = 10.1
c = "안녕"
d = True
# c가 무슨타입?
# 타입 확인방법 type(a)
print(type(a)) #int 정수
print(type(b)) #float 실수
print(type(c)) #str 문자열
print(type(d)) #bool 불타입 (참,거짓)