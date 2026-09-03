
# print("1. 컴퓨터-1_000_000")
# print("2. 세탁기-2_000_000")
# print("3. 오디오-500_000")
# choice = input("원하는 번호와 개수 입력(1/3):")

# # 1/3 은 1번을 3개 구매
# # 총 구매금액을 출력하시오
# cho = choice.split("/")
# if cho[0] =="1":
#     money = 1_000_000
#     print("컴퓨터")
#     print(int(cho[1]))
# elif cho[0] =="2":
#     money = 2_000_000
#     print("세탁기")
#     print(int(cho[1]))
# else:
#     money = 500_000
#     print("오디오")
#     print(int(cho[1]))


# print("가격:{},개수,{}총 구매금액:{}".format(money,cho[1],money*int(cho[1])))


num = input("숫자입력(1/3)")
# 앞의 숫자에는 10곱하고 뒤에 숫자에는 100곱해서 합계
#1*10+3*100 = 310

no = num.split("/")

print("{}+{}={}".format(int(no[0]),int(no[1]),int(no[0])*int(10)+int(no[1])*int(100)))