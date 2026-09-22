# c, 자바의 경우: 컴파일러 언어 - 모든 소스를 기계어로 변역후 프로그램 진행
# 파이썬: 스크립트 언어 - 한줄씩 기계어로 번역후 프로그램 진행
# 코드 재사용, 코드 간결
def d_print():
    for i in range(1,11):
        print(i)

def hello_print():
    print("안녕하세요"*5)
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

def cal(n1,n2):
    r1 = n1+n2
    r2 = n1-n2
    r3 = n1*n2
    r4 = n1/n2
    return r1,r2,r3,r4
#--------------------
d_print()
hello_print()
n1 = int(input("숫자:"))
n2 = int(input("숫자:"))
r1,r2,r3,r4 = cal(n1,n2)
print(r1,r2,r3,r4)


