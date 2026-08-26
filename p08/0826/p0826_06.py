# 산술연산자 :

# money = 12340
# 500원 동전 몇개가 필요할까요?
# result = money//500
# print("500원 동전 필요개수 :", result)
# 100원 동전 몇개가 필요할까요?
# result1 = money//100
# print("100원 동전 필요개수 :", result1)

#12340 -> 500원 동전 몇개?  100원 동전 몇개? 10원짜리 동전 몇개?

#12340원 500원 동전:?, 100원 동전:?, 10원 동전:?

# result = money//500
# result1 = (money%500)//100
# result2 = ((money%500)%100)//10
# print("500원 동전의 개수 :{} 100원 동전의 개수 :{} 10원 동전의 개수: {}".format(result,result1,result2))

# 또는
# result = money//500
# num = money%500
# result1 = num//100
# num2 = num%100
# result2 = num2//10
# print(result,result1,result2)




# 관계연산자 ==, !=, < , >, <=, >=
# True, False bool 타입으로 변환
# a = 10
# b = 5
# print(a==b) # False
# print(a!=b) # True
# print(a>b)  # True
# print(a<b)  # False


# and는 모두가 참(True)일때 참
# or은 하나라도 참(True)일때 참
# not 참이면 거짓, 거짓이면 참 EX) not(a==100) - a는 100이 아니냐? 라 참(True)
 
# 아이디, 패스워드를 입력받아 맞는지 확인
# 아이디 : aaa, 패스워드 : 1111

# id = input("아이디를 입력하세요. :")
# pw = input("패스워드를 입력하세요. :")
# if (id=="aaa") and (pw=="1111"):
#     print("로그인이 되었습니다. 메인페이지로 이동합니다.")
# else:
#     print("아이디 또는 패스워드가 일치하지 않습니다.")


# 프로그램 종료
# X(대문자)또는x(소문자)를 입력하면 종료
# str1 = input("프로그램을 종료하려면 x 또는 X를 입력하세요.")
# if (str1=="x") or (str1=="X"):
#    print("프로그램이 종료됩니다.")
# else:
#    print("프로그램을 계속 실행합니다")


