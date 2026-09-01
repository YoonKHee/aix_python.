# # aa = []
# # bb = []
# # value = 0
# # for i in range(0,100):
# #     aa.append(value)
# #     value += 2
# # print(aa)

# # for i in range(0,100):
# #     bb.append(aa[99-i])
# # print(bb)

# # cc = list(range(0,200,2))
# # print(cc) # == print(bb)

# # # 리스트내포
# # dd = [i for i in range(0,200,2)]
# # print(dd)



# aa = [10,20,30]
# print(aa*3)
# bb = [40,50,60]
# print(aa+bb) # aa,bb가 값이 변경이 안됨.
# print(aa)

# aa.extend(bb) # aa,bb가 값이 변경됨. extend
# print(aa)

# a = 1 
# b = 1
# aa.append(1) # aa값 변경
# # append, insert, extend, pop, del

# aa = [1,2,3,4,5,6,7]
# print(aa[::1])
# print(aa[::2])


# aa = [1,2,3]
# aa[1:2] = [20,30]
# print(aa[2])


# stu_list = [
#     [1,"홍길동",100,90,80,270,90.0],
#     [2,"유관순",90,80,70,240,80.0],
#     [3,"이순신",80,70,60,210,70.0]
# ]

# # stu_list[0][1] = "김유신"
# # print(stu_list)
# # print(stu_list[0][2],stu_list[0][3],stu_list[0][4])

# # 유관순 - 국어 : 100, 영어:70으로 변경출력
# stu_list[1][2] = 100
# stu_list[1][3] = 50
# stu_list[1][5] = stu_list[1][2] + stu_list[1][3] + stu_list[1][4]
# stu_list[1][6] = stu_list[1][5]/3

# print(stu_list)



# name_arr = ["홍길동", "유관순", "이순신", "강감찬", "김구"]

# name = input("검색할 이름을 입력하세요.>>")
# print(name_arr.index(name)) # 문자 fine, rfind 리스트에는 인덱스라 find로 찾을수 없음.

# while True:
#     name = input("검색할 이름을 입력하세요.>>")
#     if name in name_arr:
#         no = name_arr.index(name)
#         print(no,":",name,"학생이 검색되었습니다.")
#         Change = input("변경할 이름을 입력하세요")
#         name_arr[no] = Change
#     else:
#         print(name,"학생이 없습니다.")





stu_list = [
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0]
]

while True:
    name = input("검색이름입력:")
    for i,stu in enumerate(stu_list):
        if name in stu:
            stu_index = stu.index(name)
            print(f"있음, {stu_index}번째")
            break
    else:
        print("없음")        









