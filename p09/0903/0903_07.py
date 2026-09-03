# import sys
# print(sys.builtin_module_names)

# import math
# # dir(math)
# print(math.log(10))
# print(math.sin(10))
# print(math.floor(10.537)) # 버림 # 알아두면 좋음
# print(math.ceil(10.537)) # 올림 # 알아두면 좋음
# print(round(10.537,2)) # 반올림 # 알아두면 좋음 (값, 소숫점 자리)


# # import datetime
# from datetime import*
# now = datetime.now()
# print(now)




# from func import * # 모두 가져온다., 보통 보안때문에 잘 사용하지 않으려함


# from func import cal1,cal2,cal3 # 보통 사용하고 싶은 함수만 사용함.
# cal1()
# cal2()
# cal3()




# import func # 보안이 안좋음. 내가 만들어논 함수 보안이 안됨.
# func.cal1()
# func.cal2()
# func.cal3()


# def func(a,b,*m):
#     sum = 0
#     sum = a+b
#     for i in m:
#         sum += i
#     return sum

# print(func(1,2,3))






# def func1(*num):
#     sum = 0
#     for n in num:
#         sum += n
#     return sum

# print(func1(1,2,3))
# print(func1(1,2,))
# print(func1(10,20,30,40,50))




# def func1(a):
#     print(a)
#     return a+10


# c = 30
# result = func1(10)
# print(result)


# def func1():
#     global a #  global 전역변수에 선언되어 있는 링크를 가져옴. (모든 a를 함수안의 a값으로 치환.)
#     a = 10
#     print("func1 a:",a)

# a = 20
# func1()
# print("전역변수:",a)


# def func1():
#     a = 10 # 함수 안의 a = 지역변수
#     print("func1 a :",a)



# def func2():
#     print("func2 a :",a)


# a = 20 # 함수 밖의 a = 전역변수

# # 실행
# func1() # 10
# func2() # 20