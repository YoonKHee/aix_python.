# # 날짜함수, 랜덤함수
import datetime
import random


# now = datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)


#random
# import random
# r_no = random.randint(1,12)
# #3,4,5 봄 6,7,8, 여름 9,10,11 가을 12,1,2 겨울
# print("월 :",r_no)
# if 2<r_no<6:print("봄")
# elif 5<r_no<9: print("여름")
# elif 8<r_no<12: print("가을")
# else: print("겨울")


#랜덤 5개 뽑아내는 방법
# randint:랜덤1개, sample:랜덤 여러개(중복불가)
# shuffle:전체섞음, choices:랜덤 여러게(중복가능)
# a = random.randint(1,45) # 1개
# s = random.sample(range(1,46),5) # 여러개 1부터 46전까지 즉 45까지 5개 나란히 뽑기.
# print(s)
# # 리스트 생성방법
# # alist = [0,0,0,0,0]
# # alist1 = [0]*5
# # alist2 = list(range(1,6))

# arr1 = random.sample([1,2,3],2)
# print(arr1)
# arr2 = [1,2,3,4,5]
# random.shuffle(arr2) # 랜덤으로 섞어서 줌
# print(arr2)

# arr3 = random.choices(arr2,k=5) # 리스트 해당개수만큼 가져옴 중복가능
# print(arr3)



#1-45까지 랜덤 5개를 가져와서
#입력한 숫자가 있으면 당첨, 없으면 꽝
#1개만 우선
#5개
#비교해서 있으면 당첨, 없으면 꽝
import random

lotto = random.sample(range(1,46),5)
input0 = int(input("숫자1 :"))
input1 = int(input("숫자2 :"))
input2 = int(input("숫자3 :"))
input3 = int(input("숫자4 :"))
input4 = int(input("숫자5 :"))
input = [input0, input1, input2, input3, input4]

print("추첨숫자 :",lotto)
print("내 숫자 :",input)
# if input in lotto:print("당첨")
# else: print('꽝') 

# 반복문
for i in input:
    if i in lotto: print("당첨")
    else: print("꽝")





# a = [1,2,3,4,5]
# a[2]=30
# a.pop(1)
# a.append(200)
# print(a)