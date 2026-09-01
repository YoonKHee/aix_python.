# a_arr = [10,20,30,40,50,60,70,80,90,100]
# sum = 0
# for a in a_arr:
#     print(a)
#     sum += a
# print(sum)    

# print(a_arr[2:5])
# print(a_arr[::-1])

# 리스트 추가: append:제일 뒤에 추가, insert:위치를 지정해서 추가, extend:리스트+리스트
# 리스트 수정: a_arr[] = 1000
# 리스트 삭제: pop(위치): 위치가 없으면 제일 뒤에 삭제, del 위치값 삭제

# a_list = [1,2,3]
# a_list.append(4) # 4를 맨뒤에 추가
# print(a_list) # [1,2,3,4]
# a_list.pop()  # 맨뒤에 제거
# print(a_list) # [1,2,3]
# a_list.pop(0) # 0번째꺼 제거
# print(a_list) # [2,3]


# 퀴즈
n_arr = [100,91,230,1,2,5,70,500]
no = []
arr = []
# 100이상 숫자 출력
# 한자리 두자리 세자리 숫자 구별하기
for n in n_arr: # n타입 : 정수타입 --> 문자타입
    no = len(str(n))
    a = "{}:{}자리숫자".format(n,no)
    arr.append(a)
    print(a)
print(n_arr)


# a = 100
# b = "100"
# print(len(b))






