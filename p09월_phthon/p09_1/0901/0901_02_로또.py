# 로또 맞추기
# 4. 결과출력

import random
lotto = random.sample(range(1,46),6)
# print(lotto)

arr = []
no = []

for i in range(6):
    no = int(input("1-45사이 수:"))

    if no < 1 or no > 45:
        print("1~45 사이의 수만 입력하세요.")
        continue
    
    arr.append(no)

# no = input("1-45사이 숫자입력 : ") #문자열
    # if no.isdigit(): #문자열을 숫자로 변경가능한지
    #     no = int(input("1-45사이 숫자입력 : "))
    #     in_arr.append(no)


answer = []

for i in arr:
    if i in lotto:
        answer.append(i)

print("로또번호 :",lotto)
print("입력번호 :",arr)
print("정답갯수 :",len(answer))
print("정답번호 :",answer)



