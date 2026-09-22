# myNum = []
# i = 0
# while i<6: 
#     no = int(input("숫자입력: "))
#     if no not in myNum:
#         myNum.append(no)
#         i += 1
#     else:
#         print("이미 있는숫자")
# print("입력숫자: ",myNum)


# for i in range(6):
#     no = int(input("숫자입력: "))
#     if no not in myNum:
#         myNum.append(no)
#     else:
#         print("이미 있는숫자")
# print("입력숫자: ",myNum)



# import random
# a = random.randint(1,45)

# alist = list(range(1,46))
# random.shuffle(alist)
# print(alist)

# 랜덤으로 갯수 추출 (중복 없음)
# ranArr = random.sample(range(1,46),6)
# print(ranArr)


# 랜덤으로 개수만큼 추출 - 중복가능
# ranArr2 = random.choice(range(1,46),k=6)
# print(ranArr2)

# lotto = random.sample(range(1,46),6)
# print("로또번호 :",lotto)
# myNum = []
# i = 0
# while i<6:
#     no = int(input("내 번호:"))
#     if no not in myNum:
#         myNum.append(no)
#         i += 1
#     else: print("중복")

# # for i in range(6):
# #     no = int(input("내 번호:"))
# #     myNum.append(no)


# answer = []
# count = 0
# for i in myNum:
#     if i in lotto:
#         count += 1
#         answer.append(i)

# print("로또번호:",lotto)
# print("내 번호:",myNum)
# print("정답번호:",answer)
# print("정답갯수:",count)
    
# #6개를 입력받아 있는지 확인
# # 로또번호
# # 정답번호 : 
# # 정답갯수






