# isdigit() : 숫자인지 확인 / is
while True:
    a = input("숫자를 입력하세요")
    if a.isdigit():
        a = int(a)
        break
    else:
        print("숫자가 아닙니다")
    
print(a)



#  split분리, *전개연산자
#
# str = input("날짜입력.(2026/09/02):")
# str1 = str.split("/")
# print("{}년{}월{}일".format(*str1))
# print(str1)


#map, join -> 문자열
# stu = [1,"홍길동",100,100,100]
# # ,구분해서 문자열로 저장
# stu = list(map(str,stu))  # map 특정한 함수로 반복해줌. 
# stu2 = ",".join(stu)
# print(stu2)



# map(함수, 반복리스트)
# aa = ['1','2','3']
# alist = list(map(int,aa)) # 문자열 -> 정수타입으로 변환
# sum = 0
# for i in alist:
#     sum += i
# print(sum)


# str = input("번호 3개를 입력.(123/5/23)>>")
# # 3개 합을 구해서 출력
# list = str.split("/")
# list[0] = int(list[0])
# list[1] = int(list[1])
# list[2] = int(list[2])
# sum = list[0] + list[1] +list[2]
# print(sum)

# sum1 = 0
# for i in list:
#     sum1 += int(i)
# print(sum1)