# for i in range(10): #0,1,2,3,4,5,6,7,8,9
#     print(i)


# for i in range(1,5+1): # 0,1,2,3,4,5
#     print(i)


# for i in range(1,11,2):
#        print(i)


# 이름입력을 3번 반복하시오
# a =[]
# for i in range(3):
#     a.append(input("이름입력: ")) # 리스트 : append, insert, extend

# print("[학생명단]")
# for i in range(3):
#     print(a[i])


# for i in range(0,101,10):
#     print(i)

# for i in range(1,11):
#     print(i*10)


# arrs = [1,3,5,7]
# for i in arrs:
#     print(i)

# fruits = ["사과", "배", "바나나"]
# for f in fruits:
#     print(f)

# for in문에서 range,리스트,글자 를 넣을수 있다
# nums = [3,9,10,105,220,2,1]
# for i in nums:
#     print(i)

# for i in "안녕하세여":
#     print(i)


#입력한 숫자사 홀수인지, 짝수인지 출력하시오
# a = int(input("숫자입력: "))
# # %2==0
# if a%2==0:
#     print('짝')
# else:
#     print("홀")


# %2==0


# 반복문
# for i in range(10)/range(1,11)/range(1,11,2)/range([1,2,3])/range("안녕하세요")
# no = [3,9,10,105,220,2,1]
# for i in no:
#     # print(i)
#     # a = int(input("숫자입력: "))
#     if i%2==0:print(i,':짝')
#     else: pass
#         #print(i,":홀")


#end="" 면 프린트할때 옆으로 나란히 출력
# print(1,end="\t")
# print(2,end="\t")
# print(3)

# 구구단 출력
# for i in range(2,10):
#     #print("{}X{}={}".format(i,1,i*1))
#     print(f"{i}X{1}={i+1}")

# for i in range(2,10):
#     print(i,"단")
#     for j in range(1,10):
#         print(f"{i}x{j}={i*j}",end="  ")
#     print()


for i in range(1,10):
    for j in range(1,10):
        print(f"{i}x{j}={i*j}",end="\t")
    print()

