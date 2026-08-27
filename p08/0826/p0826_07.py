

# print(bin(10))           #1010
# print(bin(7))            #0111
# print(10 & 7)  #& 연산자  #0010  #둘다 1인것만 1.
# int("0010",2)# 10진수를 2진수로 바꾸는 방법
# 따라서 10 & 7은 0010이고, 0010은 2다.





# # 입장료 = 50000
# a = int(input("나이를 입력해주세요.:"))
# b = int(input("입장 시간을 입력해주세요:"))
# # 할인조건 = a>=65 or b>=18
# if (a>=65) or (b>=18):
#     print("최종요금은 30000원입니다")
# else:
#     print("최종요금은 50000원 입니다.")



# print("[오늘의 한마디]\n \"시작이 반이다!\"")


# print("상품코드 :{:03d}, 가격: {}원".format(7,2500))


# user_input = input("정수를 입력하세요.")
# print("입력타입:", type(user_input))
# num_float = float(user_input)
# print("실수 변환: {:.2f}".format(num_float))



age = int(input("나이를 입력하세요."))
if  age<=13 or age>=65:
    print("최종 요금은 0원입니다.")
else:
    print("최종 요금은 1500원입니다.")