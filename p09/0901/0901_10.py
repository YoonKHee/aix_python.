# # stu = {"no":1, "name":"홍길동", "kor":100, "eng":100,"math":100,"music":100}
# # stu_arr = [1,"홍길동",100,100,100,100]

# # print(stu)
# # # 딕셔너리 추가 : 없는키값 입력
# # stu["total"] = 400
# # stu["avg"] = stu["total"]/4
# # print(stu)

# # stu["kor"] = 50
# # # 딕셔너리 출력 : 키 출력
# # print("kor")
# # # 딕셔너리 삭제
# # del stu["kor"]



# stu_list = [
#     {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":100, "total":300, "avg":100},
#     {"no":2, "name":"유관순", "kor":100, "eng":100, "math":100, "total":300, "avg":100},
#     {"no":3, "name":"이순신", "kor":100, "eng":100, "math":100, "total":300, "avg":100}
#     ]
 
# print(stu_list[0]['name']) # 있는 키 입력 
# print(stu_list[0]['kor'])
# stu_list[0]['rank'] = 1 #없는키 입력은 추가가 됨
# del(stu_list[0]['no'])
# print(stu_list)

# # print(stu_list[0]['no']) # 오류가 뜨고
# print(stu_list[0].get('no')) # none 이 뜬다.




# stu = {"no":1, "name":"홍길동","total":300, "avg":100}
# for i,v in stu.items():
#     print(i,":",v,end=" ")
# print(stu.keys()) # keys 값만 나옴
# print(stu.values()) # values 값만 나온다
# print(stu.items()) # keys, values 모두 나온다
# s_list = list(stu.values()) # 딕셔너리 리스트 --> list() 타입으로 변환
# print(s_list)



# name_dic ={
#     "aaa":"토마토", "ddd":"바나나", "eee":"딸기", "bbb":"배"
# }

# import operator
# name_sort1 = []
# name_sort1 = sorted(name_dic.items(),key=lambda x:x[0]) # x:x[0]은 키값으로 배열, x:x[1]은 벨류값으로 배열
# name_sort1 = sorted(name_dic.items(),key=lambda x:x[0],reverse=True) # reverse=True는 역순정렬 

# print(name_sort1)






# engs = {
#     "car":"자동차",
#     "color":"색상",
#     "pig":"돼지",
#     "love":"사랑",
#     "phone":"전화기"
# }

# for k,v in engs.items():
#     print(k,"의 뜻:")
#     answer = input("정답:")
#     if answer == v:
#         print("정답")
#     else:
#         print("오답")



# 리스트 자동생성방법 4가지

# alist = [i for i in range(1,11)] # 리스트 내포 : 컴프리헨션
# alist2 = list(range(1,11)) 
# alist3 = [0]*10
# alist4 =[1,2,3,4,5,6,7,8,9]
# print(alist)
# print(alist2)
# print(alist3)
# print(alist4)





alist = list(range(1,21))
nlist = []
for i in alist:
    if i%3==0:
        nlist.append(i)
print(nlist)

a = [n for n in range(1,21) if n%3==0]
print(a)




