### raise 
# NotImplementedError 

# choice = int(input("번호입력:"))
# if choice==1:
#     print("학생성적입력부분")
# if choice==2:
#     print("출력")
# if choice==3:
#     print("수정")
# if choice==4:
#     raise NotImplementedError # 프로그램이 구현 안된 부분 확인.



# print(1)
# print(2)
# print(3)
# print(4)
# raise NotImplementedError
print(5)
print(6)
print(7)






# 람다식 - 함수요약


# 람다식 - 1줄만 명령어가 있어야함.
# sum = lambda n1,n2:n1+n2
# print(sum(2,20))

# map(함수,리스트)
# mList = [1,2,3,4,5] # +10// # 기본구성
# mList2 = []
# for m in mList:
#     mList2.append(m+10)
# print(mList2)


# def add(num):
#     return num+10


# mList = [1,2,3,4,5]
# a_arr = []
# for m in mList:
#     a_arr.append(add(m))


# a_arr= [m+10 for m in mList] # 리스트 내포
# print(a_arr)




#map -> map(함수,리스트)로 사용 리스트의 것들을 함수에 넣어서 만드는것.
# def add(num):
#     return num + 10

# a_lam = lambda num:num+10
# mList =[1,2,3,4,5]
# mList2 = list(map(lambda,num:num+10,[1,]))#### 외워두기
# print(mList2)




# date = ["100","200","300"]
# result = map(int,date)
# print(list(result))


# a = [1,2,3]
# b = [10,20,30]
# result = map(lambda x,y:x+y, a,b ) 
# print(list(result))

#1~4까지의 곱을 구하시오
# result = 1
# for i in range(1,5):
#     result *= i
# print(result)

# 재귀함수 자기 자신을 한번더 사용하는 함수 팩토리얼!
# def fact1(num):
#     if num<=1:
#         return num
#     else:
#         return num * fact1(num-1)

# print(fact1(5))



# #예외처리
# print(1)
# try:
#     print(2)
#     print(3)
#     print(10/0) # 에러가남
#     print(4)
# except Exception as e: # 에러가 나면 에러난 자리에 except이 껴서 돌아감 에러뒤에꺼는 사용못함
#     print(e) # except Exception as e: 는 에러 코드를 알려줌. e는 그냥 별칭(변수).
#     print(type(e))
#     print(5)
#     print(6)
# print(7)
# # 1,2,3,5,6,7






# print(1) # 구문오류

# 예외처리 # try:, except:
# 런타임에러
# arr = [1,2,3,4,5]
# while True:
#     choice = input("0-4까지 숫자입력:")
#     if choice.isdigit():
#         choice = int(choice)
#     else:
#         print("x")
#         continue



    # try:
    #     choice = int(input("0-4까지 숫자입력:"))
    #     print("선택값:",arr[choice])
    # except Exception as e:
    #     print("에러가 났습니다.")
    #     print(e)
        # if choice>4:
        #     print("입력오류")
        #     continue