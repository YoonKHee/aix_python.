# 산술연산자 : +, -, *, /, //, %, **
# 우선순위에 있는 것은 괄호로 분리
# print(2+2-2*2/2*2)
# print(2-2+((2/2)*2)+2)

# # 다른 타입 사칙연산 에러
# #print("안녕"*3)#에러
# print(1.1+5) # 6.1
# print(int(1.9)) # 1 이나옴 - 실수형을 정수형으로 변경시 소수점이 사라짐.


#문자열 던셈연산 연결연산(+) 반복연산(*)
# print("안녕"+"하세요") # 연결
# print("안녕"*10) # 반복

# 문자열 숫자인 경우 > 문자열타입을 숫자타입으로 변경 가능
# str1, str2, str3 = "100", "1.123", "9999"
# print(str1+1) # 불가능
# print(int(str1)+1) # 문자열숫자 자동 변경 안됨. int(정수형타입)으로 변경 해 주어야 함
# print(float(str2)) # 문자열숫자가 소수면 float(실수형타입)으로 변경해주어야 함
# print(int(str3)+1) 
# print(int("안녕")) # 문자를 숫자로 변환에러 문자는 숫자로 변경을 못 함. 문자가 숫자인 경우에만 가능함


#번호, 이름, 국어, 영어, 수학을 입력받아
# 번호, 이름, 국어, 영어, 수학, 합계, 평균을 출력하시오

# # 홍길동
# no = input("번호를 입력하세요.")
# name = input("이름을 입력하세요.")
# kor = int(input("국어 점수를 입력하세요."))
# eng = int(input("영어 점수를 입력하세요."))
# math = int(input("수학 점수를 입력하세요."))
# sum = kor+eng+math
# avg = sum/3


# # 유관순
# no2 = input("번호를 입력하세요.")
# name2 = input("이름을 입력하세요.")
# kor2 = int(input("국어 점수를 입력하세요."))
# eng2 = int(input("영어 점수를 입력하세요."))
# math2 = int(input("수학 점수를 입력하세요."))
# sum2 = kor2+eng2+math2
# avg2 = sum2/3

# # 천채영
# no3 = input("번호를 입력하세요.")
# name3 = input("이름을 입력하세요.")
# kor3 = int(input("국어점수를 입력하세요."))
# eng3 = int(input("영어점수를 입력하세요."))
# math3 = int(input("수학점수를 입력하세요."))
# sum3 = kor3+eng3+math3
# avg3 = sum3/3


# print("-"*115)
# print("번호\t이름\t\t국어\t\t수학\t\t영어\t\t합계\t\t평균\t\t")
# print("-"*115)
# print("{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{:.2f}\t\t".format(no,name,kor,eng,math,sum,avg))
# print("-"*115)
# print("{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{:.2f}\t\t".format(no2,name2,kor2,eng2,math2,sum2,avg2))
# print("-"*115)
# print("{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{:.2f}\t\t".format(no3,name3,kor3,eng3,math3,sum3,avg3))
# print("-"*115)




# print("101"+"102") #101102
# print("안녕"+"하세요")#안녕하세요


# a = 10
# a = a+2 # a += 2는 같은 값이 나온다 이유는 속도가 쪼금 더 빨라지기 때문에
# a += 2  # 하지만 지금은 컴퓨터 속도가 빠른편이라 이렇게도 쓴다 라는 것만 알아두면 됨
# print(a)



# 원의 반지름을 입력받아
# 원의 넓이를 출력하시오 # ㅠr**2 #ㅠ = 3.14
# 원의 둘레 : 2*pi*length
pi = 3.14
length = int(input("반지름을 입력하시오."))
print("원의넓이{}\t원의 둘레{:.2f}".format(pi*(length**2),2*pi*length))




