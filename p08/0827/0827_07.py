# 리스트 = 배열
# a = 1
# arr = [1,2,3,4,5,6,7,8,9]
# print(a)        #1
# print(type(a))  #int
# print(a+1)      #2

# print(arr)       # [1,2,3,4,5,6,7,8,9]
# print(type(arr)) # list
# print(arr[1]+1)  # 3 ->arr[1]==2, 2+1
# print(len(arr))  # 리스트의 개수 : length줄임


# 리스트는[]시작
# 리스트는 여러개를 저장
# 리스트는 0부터 주소가 시작
# 리스트를 print하면 모두 출력가낭
# 리스트의 특정주소로 그 값을 출력할수았음,
# 리스트 개수:len()
# 리스트 안에는 모든 타입에 넣을수 있음
# - 정수, 실수, 문자열, 불, 리스트, 튜플, 딕셔너리 # 튜플, 딕셔너리는 리스트와 비슷한 식. 


# 리스트 추가 가능 타입: 모든 타입이 가능
# arr = [1,"안녕", 1.2,True,[1,3,4]]
# print(arr[1],arr[3],arr[4])
# print(arr[4][1]) # arr4 에서 3을 출력하고 싶을때
# a = arr[4]
# print(a[1]) # 결과값은 위와 같음 


#1-10 사이의 숫자 3개를 입력받아 
# 랜던 숫자를 맞추면 당첨, 그렇지 않으면 꽝

# import random
# a = random.randint(1,10)

# 반복문을 사용할수 없음.
# 일반변수는 반복문을 사용하기 힘듦.
# no1 = int(input("입력숫자"))
# no2 = int(input("입력숫자"))
# no3 = int(input("입력숫자"))
# print("입력숫자 :",no1,no2,no3)

# num = [0,0,0]
# num[0] = int(input("입력숫자 1:"))
# num[1] = int(input("입력숫자 2:"))
# num[2] = int(input("입력숫자 3:"))
# print("입력숫자 :", num)
# print(a)
# if a==num: print("당첨")
# else: print("꽝")



# a = "사과"
# b = "딸기"
# c = "수박"
# d = "참외"
# e = "복숭아"
# a b c d e 중 참외가 있는지 확인하고,
# 있으면 참외가 있다, 없으면 참외가 없다.

# if a=="참외" or b=="참외" or c=="참외" or d=="참외" or e=="참외":print("o")
# else: print("x")

# 비교시, 리스트는 ("검색내용" in 리스트) 하면됨.
# 리스트
# fruit_list = ["사과", "딸기", "수박", "참외", "복숭아"]
# if "참외" in fruit_list:print("o")
# else: print("x")


# import random
# r_no = random.randint(1,10)
# # 3개 숫자 입력
# arr =[]
# # 리스트의 값을 추가할시 append사용
# arr.append(int(input("1. 1-10 숫자입력:")))
# arr.append(int(input("2. 1-10 숫자입력:")))
# arr.append(int(input("3. 1-10 숫자입력:")))
# print(arr)
# print(r_no)


# if r_no in arr:
#     print("o")
# else:
#     print("x")

# 위에것을 줄여 쓰면
# if r_no in arr:print("o")
# else:print("x")

# 위에것을 더 줄여 쓰면
# print("당첨") if r_no in arr else print("x")


# fruit = ["사과", "딸기", "수박", "참외", "복숭아"]

# print(fruit[2]) # 딸기
# print(fruit[1:4]) # 1번부터 4번 앞에꺼까지 #딸기, 수박, 참외
# print(fruit[2:]) # 2번부터 끝까지 출력 # 수박 참외 복숭아
# print(fruit[:3]) # 처음부터 3번 앞에꺼까지 # 사과 딸기 수박
# print(fruit[:])  # 모두출력
# print(fruit[::2]) # [첫칸은 시작, 두번째 칸은 끝, 세번째 칸은 간격] # 2칸씩 건너뛰어서 출력할거다 # 사과 수박 복숭아

# 슬라이싱 [시작,끝,간격]
# arr = [1,2,3,4,5,6,7,8,9]
# print(arr[::2]) # 홀수번째만 뽑아올때 # 처음부터 끝까지 2칸씩 출력할거다 # 1,3,5,7,9
# print(arr[1::2]) # 짝수번째만 뽑아올때 # 1번쨰부터 끝까지 2칸씩 출력할거다 # 2,4,6,8
# print(arr[:-1]) # 처음부터 -1빼고(뒤에서 하나빼고) 전부 출력 # 1 2 3 4 5 6 7 8
# print(arr[::-1]) # 리스트 역순정렬



# 문자열 - 리스트형태로 저장
# name = "안녕하세요반갑습니다"
# print(name) # 안녕하세요반갑습니다
# print(name[1]) # 녕
# print(name[6]) # 갑
# print(name[5:8]) # 반갑습
# print(name[::-1])# 다니습갑반요세하녕안
# print(name[::2]) # 안하요갑니
# if "하" in name:print("있다")
# else: print("없다")
# 줄이면
# print("있다") if "하" in name else print ("없다") 



# arr = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# arr = [[1,2,3],[4,5,6],[7,8,9]]

# print(arr[1])       #[4,5,6]
# print(arr[1][1])    # 5


# arr1 = [1,2,3]
# arr2 = [4,5]
# arr3 = arr1+arr2 # 리스트+리스트 = 리스트 합쳐짐 [1,2,3,4,5]
# print(arr1+arr2)
# print(arr3)

# arr4 = arr1*3 # arr1을 반복함 [1,2,3,1,2,3,1,2,3]
# print(arr4)


# aaa = [0,0,0,0,0,0,0,0,0,0]
# aaa1 = [0]*10 # =[0,0,0,0,0,0,0,0,0,0]
# #   aaa = aaa1 , [::-1], [::2], [1:3] 이런 유형은 외워두기, [:-1]은 제일 끝에꺼 빼고 출력해라
# print(aaa)
# print(aaa1)


# 리스트추가 : append, insert

# arr = [1,2]
# # append : 제일 뒤쪽에 추가
# arr.append(3) # [1 2 3]
# arr.append(5) # [1 2 3 5]
# arr.append(7) # [1 2 3 5 7]
# print(arr)
# #arr = [1 2 3 5 7]
# arr.insert(1,20) # [1 20 2 3 5 7] #insert :원하는 위치에 추가 # insert는 잘 사용하지 않음, 효율이 떨어짐.
# print(arr)



# 리스트 삭제
# a = [1,2,3]
# b = [4,5,6]
# print(a+b) #는 원본인 a는 그대로인데 # 원본에 영향이 없음

# a.extend(b)# extend는 원본의 값을 직접 변경해서 추가해줌 # 자주 사용하지는 않음. 원본에 지장이 생김
# print(a) # [1 2 3 4 5 6] 이됨 


# 리스트 삭제 - del, pop, remove, clear(모두삭제)
# arr = [1,2,3,4,5,True,"안녕"]
# # pop
# arr.pop(2) # 2번째 인덱스를 삭제한다
# print(arr) # [1,2,4,5] # 삭제도 왠만하면 제일 끝에꺼 삭제하는게 효율이 좋음.

# del arr[0]
# print(arr)

# arr.remove("안녕")
# print(arr)


# 정렬. 순차정렬(sort), 역순정렬 sort(reverse=True)
# arr = [1,5,8,3,2]
# arr.sort() # 순차정렬 # [1 2 3 5 8]
# print(arr)
# arr.sort(reverse=True) # 역순정렬 #[8 5 3 2 1]
# print(arr)


# 원하는 값 in 리스트, 원하는값 not in 리스트
# arr = [1,3,5,7,9]
# if 7 in arr:
#     print("o")
# else:
#     print("x")