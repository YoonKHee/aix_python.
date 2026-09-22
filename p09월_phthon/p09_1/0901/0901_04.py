# 전개연산자
# arr1 = [1,2,3,4,5]
# arr2 = []
# a = 1 # 1을 a에 넣은것 
# print(a) # 1
# a2 = 0 # a2 에 0을 넣은것
# print(a2) # 0
# a2 = a # a2에 a를 넣은것 
# print(a2) # 1
# a = 100 # a에 100을 넣은것
# print(a2) # 1 , a값에 100을 넣은 것이지. a2는 그 전에 넣은 값인 1이다.

# print(a2)
# print(arr1)
# print(*arr1) # 리스트에서 하나씩 빼서 전개하겠다. # 전개연산자


# # 얕은복사:두 리스트가 상관관계가 생김 ,깊은복사:두 리스트가 상관관계 없이 생김
# arr1 = [1,2,3,4,5]
# arr2 = []
# arr3 = []
# arr2 = arr1 # 얕은복사
# # print(arr1) # [1,2,3,4,5]
# # print(arr2) # [1,2,3,4,5]
# arr1[2] = 1000
# # print(arr1) # [1,2,1000,4,5]
# # print(arr2) # [1,2,1000,4,5] - 리스트는 주소값이 같아서 같이 바뀐다.
# arr3 = [*arr1] # 깊은복사 *arr1 리스트 주소값이 아닌 개별값을 넣아주는 것 
# # print(arr3) # [1,2,1000,4,5] 
# arr1[2] = 500  
# # print(arr3) # [1,2,1000,4,5] 
# # print(arr1) # [1,2,500,4,5] 


arr1 = [1,2,3,4,5]
arr2 = []
arr3 = []
arr2 = arr1 # 얕은복사
arr3 = [*arr1] # 깊은복사
print(arr1)
print(arr2)
print(arr3)
print("-"*60)
arr2[0] = 5
print(arr1)
print(arr2)
print(arr3)
