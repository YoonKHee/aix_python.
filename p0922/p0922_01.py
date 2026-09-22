# 1에서 100까지 랜덤숫자를 1개 생성
# 무한 반복해서 숫자를 맞추는 프로그램을 구현
# 입력한 숫자가 크면 크다
# 입력한 숫자가 작으면 작다라고 출력하고
# 맞추면 정답이라고 출력후 프로그램 종료
# 입력한 숫자가 모두 출력되도록 하시오.
import random
ran_no = random.randint(1,100)
arr_no = []
while True:
    input_no = int(input("숫자입력:"))
    arr_no.append(input_no)
    if input_no == ran_no:
        print("일치 합니다.")
        break
    elif input_no > ran_no:
        print("입력한 숫자가 더 크다")
    else :
        print("입력한 숫자가 더 작다")


print("랜덤숫자:", ran_no)
print("입력한숫자:", arr_no)
