# break : 반복문을 완전 종료
# continue : 1번만 제외 이후 계속 반복

# for i in range(100):
#     if i==50:
#         continue
#     print(i)
# print("프로그램 종료")
# no = []
# name = []
# i = 1 # 번호
# while True:
#     n = input(f"{i}.이름:")
#     if n =="0":break
#     name.append(n)
#     no.append(i)
#     i = i+1

# print("프로그램 종료")


# 1-100까지 랜덤숫자 1개를 생성

# import random
# ran1 = random.randint(1,100)
# # 랜덤숫자를 맞출때까지 무한반복 프로그램을 구현하시오
# myNum = 0
# myList = []
# while True:
#     myNum = int(input("1~100 사이 숫자:"))
#     myList.append(myNum)
#     print("내 숫자",myNum)
# # 랜덤숫자와 입력숫자가 같은지 비교
#     if myNum == ran1:
#         print("일치")
#         break
#     elif myNum>ran1:
#         print("입력숫자가 더 큼, 작은수 입력")
#     elif myNum<ran1:
#         print("입력숫자가 더 작음, 큰수 입력")

# print("입력한 숫자:",myList)
# print("정답: ",myList[-1])        
# print(f"랜덤숫자:{ran1}.프로그램을 종료합니다.")




# 입력한 숫자와 랜덤숫자가 몇개가 일치하는지 갯수 출력
# import random
# ranNo = random.randint(1,10)
# ranNo = [1,5,9,6,7]
# inputNo = [1,2,3,4]
# answerNo = []
# count = 0
# for i in inputNo:
#     if i in ranNo:
#         count = count+1
#         answerNo.append(i)
#         print("있음")
#     else: print("없음")
# print("개수 :",count)


# 입력한 슛자를 모두 저장해서 프로그램을 종료할때 출력하시오.
noArr = [10,40,2,9,5]
no = []
answer = []
count = 0
while True:
    i_no = int(input("입력 숫자:"))
    no.append(i_no)
    if i_no ==0:break
for i in no:
    if i in noArr:
        count = count+1
        answer.append(no)

print("종료되었습니다. 입력된 숫자",no)
print("정답:",answer)
print("정답갯수",count)



    # 1. 입력한 숫자 리스트에 저장

    # 2. 0을 입력할때 반복문 break

# 3. 반복문 종료시, 입력된 숫자 모두 출력



