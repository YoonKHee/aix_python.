# # for 변수 in 범위: 
# for i in range(10):
#     print(i)

# for i in range(5):
#     print(i*10)

# for i in range(1,6):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in [1,2,4,6]:
#     print(i)

# arr = list(range(1,11))
# print(arr)



# for _ in range(10):
#     print("안녕")


# for i in range(2):
#     print(i+1,"번째")
#     no = i+1
#     name = input("이름 :")
#     kor = int(input("국점: "))
#     print("{}\t{}\t{}".format(no,name,kor))


# for i in range(1,10):
#     print(f"2 X {i} = {2*i}")


# sum = 0
# for i in range(1,11):
#     sum = sum+i
#     if sum>10:
#         print("10보다 크기 바로 앞일때:",i-1)
#         print("10초과 전 시점:",sum-i)
#         break

# print("합계 :",sum)


# 합계가 100이 넘어가는 시점은 숫자가 얼마일때 일까요?


# for i in range(1,10):
#     # print(f"2 X {i} = {2*i}")
#     for j in range(1,10):
#         print("{} X {} = {}".format(i,j,j*i))


# for i in range(1,10):
#     for j in range(1,10):
#         print((i*10)+j+1,":",i,j)



#번호표
# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             print("번호표:{}{}{}".format(i,j,k))
#             #print("번호표:",i,j,k)



# 반복문을 사용해서 1-100 합을 출력
# sum = 0
# for i in range(1,101):
#     sum = sum+i
# print("합: ",sum)

# 200을 넘는 시점의 i값과 i번째 합계를 출력
# sum = 0
# for i in range(1,101):
#     sum = sum+i
#     if sum>200:
#         break
# print("200넘는 시점 {}, 그때의 합{}: ".format(i,sum))

# 200을 넘는 이전 시점의 i,합계 를 출력
# sum = 0
# for i in range(1,101):
#     sum = sum+i
#     if sum>200:
#         break
# print("200넘는 전 시점 {}, 200전까지의 합{}: ".format(i-1,sum-i))

# 구구단 출력

# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i} X {j} = {i*j}")



# 반복문엔 리스트가 필요함 그래야 많은양에 유리함.
# name = []
# kor = []
# for i in range(2):
#     name.append(input("이름 :"))
#     kor.append(int(input("국어 :")))

# for i in range(2):
#     print("{}\t{}".format(name[i],kor[i]))



# # 다른방법
# name = []
# kor = []
# stu = []
# for i in range(2):
#     name = input("이름 :")
#     kor = int(input("국어 :"))
#     stu.append([name,kor])

# for i in range(2):
#     print("{}\t{}".format(*stu[i]))



# # 3개일때의 방법
# name = []
# kor = []
# stu = []
# for i in range(2):
#     no = i+1
#     name = input("이름 :")
#     kor = int(input("국어 :"))
#     stu.append([no,name,kor])

# for i in range(2):
#     print("{}\t{}\t{}".format(stu[i][0],stu[i][1],stu[i][2]))




name = []
kor = []
eng = []
math = []
sum = []
avg = []
for i in range(3):
    no = i+1
    name.append(input("이름 :"))
    kor.append(int(input("국어 :")))
    eng.append(int(input("영어 :")))
    math.append(int(input("수학 :")))
    sum.append(int(kor[i]+eng[i]+math[i]))
    avg.append(sum[i]/3)
for i in range(3):
    print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(i+1,name[i],kor[i],eng[i],math[i],sum[i],avg[i]))
