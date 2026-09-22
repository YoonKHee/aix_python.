# a_arr = [1,5,10,20,90,100,7,2]
# a_arr2 = [*a_arr]
# a_arr3 = a_arr.copy() 
# a_arr2.sort() #밑에 2개랑 같은 뜻임
# a_arr2.sort(reverse=True) #밑에 위에랑 같은뜻
# a_arr2.reverse() # 위의 2개가 같은뜻
# a_arr[0] = 100
# print(a_arr)
# print(a_arr2)
# print(a_arr3)


# aa = list(range(1,13))
# print(aa)

# a_arr = []
# for i in range(0,12,4):
#     a_arr.append(aa[i:i+4])

# print(a_arr)

#------------------------
# import random

# aa = list(range(1,26))
# random.shuffle(aa)
# for i, v in enumerate(aa):
#     if (i+1)%5==0:
#         print(v,end="\t")
#         continue
    
#     if i%5!=0:
#         print(v,end="\t")
#     else: print(v)


import random

a_arr = list(range(1,26))
random.shuffle(a_arr)
while True:
    print(" "*18,end="")
    print(" [빙고게임]")
    print("-"*50)
    for i,v in enumerate(a_arr): # i:인덱스, v :값 # enumerate 인덱스와 값을 동시에 가져오는 함수.
        if (i+1)%5!=0:
            print(v,end="\t")
        else:
            print(v)
    print("-"*50)
    num = int(input("원하는 번호 입력:"))
    if num < 0 or 25 < num:
        print("범위에 벗어난 숫자입니다.")
        continue
    if num in a_arr:
        idx = a_arr.index(num)
        a_arr[idx] = "x"




