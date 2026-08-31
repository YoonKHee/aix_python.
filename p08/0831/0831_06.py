# 1-100사이의 랜덤 번호를 맞추는 프로그램 구현
# 랜덤번호보다 높은수를 입력하면 낮은 숫자입력!!, 높으면 높은숫자입력!
# 정답을 맞추면 
# 정답숫자 :
# 숫자입력 횟수:
# 입력한 수: 모두 출력할것

# import random
# answer = random.randint(1,100)
# print(answer)
# i = 0
# myNum = []
# while True:
#     i = int(input("숫자 입력:"))
#     myNum.append(i)
#     if i == answer: 
#         print("일치!")
#         break

#     elif i > answer: 
#         print("작은수입력!!")
#     elif i < answer: 
#         print("큰수입력!!")
# print(f"정답숫자:{answer}\t숫자입력횟수:{len(myNum)}\t입력한수{myNum}")







# import random
# lotto = random.sample(range(1,46),6)

# myNum = []
# answer = []
# count = []

# i = 0
# while i<6:
#     no = int(input("내 번호:"))
#     if no > 45 or no < 1: 
#             print("1~45까지 입력")
#             continue
#     if no not in myNum:
#         myNum.append(no)
#         i += 1
#     else : print("중복")

# count = 0
# for i in myNum:
#     if i in lotto:
#         count += 1
#         answer.append(i)

# print("로또번호:",lotto)
# print("내번호:",myNum)
# print("정답번호:",answer)
# print("정답갯수:",count)




# 6개를 입력받아 있는지 확인
# 로또번호
# 내번호
# 정답번호 : 
# 정답갯수




# 1-100사이의 랜덤 번호를 맞추는 프로그램 구현
# 랜덤번호보다 높은수를 입력하면 낮은 숫자입력!!, 높으면 높은숫자입력!
# 정답을 맞추면 
# 정답숫자 :
# 숫자입력 횟수:
# 입력한 수: 모두 출력할것


import random
ran = random.randint(1,100)
num = []
i = 0
while True:
    my = int(input("수 입력:"))
    num.append(my)
    if my == ran: 
        print("일치")
        break
    elif my <ran:
        print("큰수입력") 
    elif my >ran:
        print("작은수입력") 

print("정답숫자:",ran)
print("숫자입력 횟수:",len(num))
print("입력한수 :",num)






