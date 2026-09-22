def a():
        for i in range(2,10):
            print(i,"단")
            for j in range(1,10):
                    if j ==9:
                        print(f"{i}x{j}={i*j}")
                    else:
                        print(f"{i}x{j}={i*j}",end="\t")

def b():
    n1 = int(input("1번수:"))
    n2 = int(input("2번수:"))
    print("합:{},차:{}".format(n1+n2,n1-n2))


def c():
    sum = 0
    for i in range(1,11):
        sum += i
    print(sum)    

print("1. 구구단 출력")
print("2. 두 수를 입력받아 +, - 값을 출력")
print("3. 1-10까지 합을 출력")
choice = int(input("원하는 번호:"))

if choice ==1:
    a()
elif choice ==2:
    b()
else:
    c()
