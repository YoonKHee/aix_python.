# Quiz
# 1-100까지 랜덤숫자 3개를 만들어서
# 입력한 숫자 1개가 있는지를 확인해서
# 있으면 당첨, 없으면 꽝
# 랜덤숫자 리스트 출력
# 입력숫자 출력
# 중복없이 arr = random.sample(range(1,101),3) 1~100까지 중복되지 않게 3개를

# import random
# # r_no = random.randint(1,100)
# # r_no1 = random.randint(1,100)
# # r_no2 = random.randint(1,100)
# r_no0 = random.sample(range(1,11),3)

# no = int(input("1. 숫자입력:"))
# r_no0.sort()
# print("입력숫자",no)
# print("랜덤숫자 :",r_no0)

# if no in r_no0:
#     print("당첨")
# else:
#     print("꽝")



# 컴퓨터가 3개의 동전을 던집니다. 
# 동전의 앞면은 1, 뒷면은 0입니다.coin1, coin2, coin3 변수에 각각 무작위로 0 또는 1을 저장하세요.
# 사용자에게 예측값(0 또는 1)을 입력받아, 
# 컴퓨터가 던진 3개의 동전 결과 중에 내가 입력한 값이 하나라도 있으면 "하나는 맞췄다!", 없으면 "전부 틀렸다!"를 출력하세요.


# import random

# coin1 = random.randint(0,1)
# coin2 = random.randint(0,1)
# coin3 = random.randint(0,1)

# my = int(input("동전 앞은1 뒤는0 입력 :"))

# print("내가 입력한 수 :",my)
# print("랜덤으로 뽑은수",coin1,coin2,coin3)

# if my in[coin1,coin2,coin3]:
#     print("당첨")
# else:
#     print("꽝")




# 컴퓨터가 1부터 10까지의 무작위 숫자 3개를 
# 각각 독립된 변수 scout1, scout2, scout3에 저장합니다.
# 사용자에게 타겟 숫자 1개를 입력받은 후, 
# 그 숫자가 컴퓨터 삼총사 숫자 중에 존재하면서 
# 동시에 그 숫자가 5보다 큰지(and) 확인하여 맞다면 "작전 성공", 아니면 "작전 실패"를 출력하세요.



# import random
# scout1 = random.randint(1,10)
# scout2 = random.randint(1,10)
# scout3 = random.randint(1,10)
# no = int(input("숫자입력:"))
# print("랜덤수 3개: ",scout1,scout2,scout3)
# print("입력수:",no)
# if no in[scout1,scout2,scout3] and no>5:
#     print("작전성공")
# else:
#     print("작전실패")


# name = input("이름 :")
# kor = int(input("국어점수 입력:"))
# eng = int(input("영어점수 입력:"))
# avg = (kor+eng)/2

# if avg>=90:
#     grade = "A"
# elif avg>=80:
#     grade ="B"
# elif avg>=70:
#     grade ="C"
# elif avg>=60:
#     grade ="D"
# else:
#     grade ="F"

# print("="*25)
# print("{}학생 성적표".format(name))
# print("평균점수 :",avg)
# print("최종학점 :",grade)
# print("="*25)



age = int(input("나이 :"))
print("나이 :",age)
if age>=65: print("경로우대: 무료")
elif 20<=age<=64: print("성인: 14,000원")
elif 8<=age<=19: print("청소년: 9,000원")
else: print("어린이: 무료")


import random
lotto = random.sample(range(1,46),6)
lotto.sort()
b_no = int(input("보너스 번호:"))
print("로또번호: ",lotto)

if b_no in lotto:print("당첨확률상승!")
else: print("아쉽지만 다음 기회에!")
            