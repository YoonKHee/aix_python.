# 함수사용이유 : 긴 구문의 반족적인 명령어를 줄일수있음
# 코드를 간결하게 하기 위해서 함수 사용

def stu_print():
    for s in stu:
        print("{},{},{},{},{}".format(*s))

stu = [
    [1,"홍길동",100,100,100],
    [1,"유관순",100,100,100],
    [1,"이순신",100,100,100]
]

while True:
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")
    choice = int(input("번호입력:"))
    if choice ==1:
        name = input("이름입력:")
        stu_print()

    elif choice ==2:
        # 학생출력구문
        print("번호\t이름\t국어\t영어\t수학")
        stu_print()
    else:
        name = input("이름입력:")




# def cal():
#     num1 = int(input("숫자입력"))
#     num2 = int(input("숫자입력"))
#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)

# cal()


# def fun():
#     print("함수 호출")

# fun()