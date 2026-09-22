# 구구단을 아래로 출력하시오
# 구구단을 옆으로 출력하시오

# for i in range(1,10):
#     print(i,"단")
#     for j in range(1,10):
#         print(f"{i}x{j}={i*j}")





# sum = 0
# result = 1
# for i in range(1,101):
#     sum = sum+i
#     result = sum*i
# print("합:",sum)
# print("곱:{:,}".format(result))

# sum 100넘을때

# sum = 0
# no = 0
# sum2 = 0
# for i in range(1,101):
#     sum = sum+i
#     if sum>100:
#         no = i
#         sum2 = sum
#         break
# print(f"합계가 100을 넘을때 i의 값:{i}, 그때의 합계{sum2}.")
# print(f"이전 단계{i-1}, 그때의 합{sum2-i}")


# 1-100까지의 합 출력
# sum=0
# for i in range(1,101):
#     sum = sum + i
# print(sum)

# 홀수 합 구하기

# sum1=0
# for i in range(1,101,2):
#     sum1 = sum1 + i
# print(sum1)


# sum=0
# for i in range(1,101):
#     if i%7==0:
#         sum = sum + i
# print(sum)


# 3개의 입력한 숫자의 합을 구하시오

# sum = []
# for i in range(3):
#     sum.append(int(input("수:")))
# print("입력값:",sum)
# sum1 = sum[0]+sum[1]+sum[2]
# print("합계:",sum1)

# sum = 0
# for i in range(1,10+1):
#     sum += i # =sum = sum + i
# print(sum)



# 입력한 첫번째 숫자부터 두번째 입력한 숫자까지 합[2,5]
# a = int(input("1번째수: "))
# b = int(input("2번째수: "))
# c = 0
# sum = 0
# if a>b: # a가 클때만 값을 서로 변경
#     a,b = b,a # a,b위치를 바꾸겠다는뜻
#     # c = a
#     # a = b
#     # b = c
# for i in range(a,b+1):
#     sum = sum+i
# print(sum)


#구구단 출력 숫자 입력을받아 5단부터 출력
# 5단만 출력
# a = int(input("단:"))
# b = int(input("단까지:"))
# for i in range(a,a+1):
#     print(i,"단")
#     for j in range(1,b+1):
#         print(f"{i}x{j}={i*j}",end="\t")
#     print()



# a = ["바나나", "딸기", "사과"]
# for i in range(3):
#     a.append(input("과일:"))
# print(a)
# for i in a:
#     print(i)
    

# a = ["바나나", "딸기", "사과","배","복숭아"]
# j = 1 
# for i in a:
#     print(j,":",i) # 1:바나나, 2:딸기, 3:사과
#     j = j+1

# for i,value in enumerate(a): #index번호, 리스트값 2개 동시에 전달
#     print(i,":",value)

# for i in range(len(a)): # len을 쓰면 a값의 양이 늘어날수록 같이 늘어남
#     print(i,":",a[i])


# no = []
# name = []
# kor = []
# eng = []
# math = []
# total = []
# avg = []
# for i in range(3):
#     no.append(input("번호:"))
#     name.append(input("이름:"))
#     kor.append(int(input("국어점수:")))
#     eng.append(int(input("영어점수:")))
#     math.append(int(input("수학점수:")))
#     total.append(kor[i]+eng[i]+math[i])
#     avg.append(total[i]/3)
    
# print("[학생성적]")
# print("이름\t국어\t영어\t수학\t합계\t평균")
# for i in range(len(no)):
#     print(f"{no[i]}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\t{total[i]}\t{avg[i]:.2f}")    
    

# enumerate : 번호, 값 2개가 동시에 전달이 됨
# a_list = ["딸기", "바나나", "사과"]
# for i, v in enumerate(a_list): 
#     print(i,":",v)


# for i in range(10): for문에 사용 가능한것들 #range(1,11,2)/[리스트]/문자열


# alist = []
# print(len(alist)) # 0개
# alist2 = [0,0,0]
# print(len(alist2)) # 3개 
# alist3 = [0]*10
# print(len(alist3)) # 10개
# alist4 = list(range(10))
# print(alist4)

# alist5 = [i*i for i in range(10)] # 리스트 내포 포문을 리스트에 넣는다 # i*i처럼 안의 값을 계산하고 싶을때 사용 
# print(alist5) # alist4와 동일한 뜻 안의 값을 계산해서 나타내고 싶을때 사용


