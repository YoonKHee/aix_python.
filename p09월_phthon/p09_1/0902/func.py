
def ran_number(choice):
    if choice == 1:
        # 랜덤숫자 5개
        result = random.sample(range(1,100),5)
    elif choice ==2:

        #3개
        result = random.sample(range(1,100),3)
    else:
        #1개
        result = random.sample(range(1,100),1)
    return result


def main_print():
        print("1. 랜덤숫자 5개 가져오기")
        print("2. 랜덤숫자 3개 가져오기")
        print("3. 랜덤숫자 1개 가져오기")
        choice = int(input("원하는 번호를 입력.>>"))
        return choice



def a():
    print("1. 구구단 출력 프로그램")
    print("2. 1-10까지 숫자 맞추기 프로그램")
    print("3. 두수를 입력받아 +,-,*,/ 결과값 출력 프로그램")
    choice = int(input("번호입력:"))
    return choice

def b():
    for i in range(1,10):
        print(i,"단")
        for j in range(1,10):
            print(f"{i}x{j}={i*j}",end="\t")
            if j ==9:
                print(f"{i}x{j}={i*j}")
    print()
    pass

def c():
    import random
    ran = random.randint(1,10)
    my = (int(input("내숫자:")))
    if my == ran:
        print("정답")
    else:
        print("오답")
    print(f"정답숫자:{ran}, 내숫자:{my}")  

def d():
    num1 = int(input("숫자1:"))
    num2 = int(input("숫자2:"))
    print(f"합:{num1+num2}차:{num1-num2}곱:{num1*num2}나:{num1/num2}")
    pass
