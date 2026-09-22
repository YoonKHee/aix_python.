# # 반복문 : for-반복/회수지정, while-조건
# import random
# ran_no = random.randint(1,100)
# in_no = 0 # 입력변수
# in_arr = [] # 입력한 모든 숫자 리스트 저장
# while True:
#     in_no = int(input("1-100사이의 자연수:"))
#     in_arr.append(in_no)
#     if in_no == ran_no:
#         print("정답")
#         break
#     elif in_no <ran_no:
#         print("큰수입력:")
#     elif in_no >ran_no:
#         print("작은수입력:")
# print("입력한 모든 리스트:", in_arr)
# print("정답:", in_arr[-1])






# 1-100사이의 숫자 맞추기
# 1. 랜덤번호 1개 생성
# 2. 무한으로 입력받기
# 3. 숫자를 입력받기
# 4. 랜덤번호와 숫자 비교
# 5. 결과 출력


import random
ran = random.randint(1,100)
mynum = []
arr = []
while True:
    no = int(input("내 숫자:"))
    mynum.append(no)
    if no == ran:
        print("정답:")
        brea
    elif no < ran:
        print("큰수입력:")
    elif no > ran:
        print("작은수 입력:")
print("내가 입력한 수:", mynum)
print("정답번호: ",ran)
print("입력횟수:",len(mynum))



