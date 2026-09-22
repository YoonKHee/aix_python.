# alist = [1,2,3]
# alist2 = []
# alist2 = alist # 얕은복사
# alist[0] = 100
# print(alist2)


# alist = [1,2,3]
# alist2 = []
# alist2 = [*alist] # 깊은복사
# alist[0] = 100
# print(alist2)


# # aa = ["바나나","딸기","사과","딸기","딸기","사과"]
# aa = [1,2,3,1,1,1,2,3,2,2,1,3,1,2,3]
# # print(aa.count("바나나"))
# # print(aa.count("사과"))
# # print(aa.count("딸기"))
# aa_dic = {}
# for a in aa:
#     if a not in aa_dic:
#         aa_dic[a] = 1
#     else: 
#         aa_dic[a] += 1
#         print("있습니다")
# print(aa_dic)    


# # 딕셔너리
# a_dic = {"바나나":1, "딸기":2, "사과":2}
# # 출력
# print(a_dic["바나나"]) 
# # 추가
# a_dic["배"] = 5 
# print(a_dic)
# # 삭제 
# del a_dic["바나나"]
# # 수정 
# print(a_dic)
# a_dic["사과"] = 100
# print(a_dic)

# 리스트 생성 방법
# a1 = [1,2,3,4,5]
# a2 = [0]*5
# a3 = list(range(1,6))
# a4 = [i for i in range(1,6) if i%2==0] # 리스트 내포
# print(a4)


# a = [1,2,3,4,5]
# b = [10,20,30,40,50]
# c = []

# c = list(zip(a,b))
# d = dict(zip(a,b))
# [] () 는 같은데 []는 수정 가능하고, ()수정불가능.
# for i,j in zip(a,b): # 두개 동시에 돌릴때 zip
#     c.append([i,j])

# for i in range(len(a)):
#     c.append([a[i],b[i]])

# print(c)
# print(d)



# aa = "가나다라가가가나나다라라라라라라라"
# aa1 = {}
# # {가 :10 ,나:  ---}
# for i in aa:
#     if i not in aa1:
#         aa1[i] = 1
#     else:
#         aa1[i] += 1
# print(aa1)


# aa = "a/b/c/d/e/f/g"
# aal = aa.split("/")
# print(aal)

# bb = "100,11,14,5,7"
# # 모든수의 합
# bbl = bb.split(",")
# bbl = [int(i) for i in bbl]
# print(bbl)
# sum = 0
# for b in bbl:
#     sum += b
# print(sum)


# ss = "파이썬 공부!! 열심히 합시다. 파이썬"
# print(ss.count("공부")) # 1
# print(ss.count("파이썬")) # 3
# print(ss.find("공부")) # 4
# print(ss.find("자바")) # 없으면 -1
# print(ss.index("자바")) # index는 없으면 에러



# aa = input("이름을 입력하세요.>> ").strip() # strip 공백을 제거해줌

# ss = "    파이썬"          # 파이썬 strip
# ss2 = "<<<<파<이<<썬<<<"   # 파이썬 replace

# print(ss.strip())
# print(ss2.replace("<",""))


#join



### 앞뒤공백제거 - strip()
a = "      a b c      "
print(a.strip()) # 공백제거 -> a반영은 안됨.

# 중간공백제거 : replace
print(a.replace(" ",""))
### 분리 : split - 리스트타입으로 변환
c = "딸기,수박,바나나,사과"
print(c)
print(c.split(","))


d = "1,홍길동,100,100,100,300,100.0"
dlist = d.split(",")
dlist[2] = 90
dlist[3] = int(dlist[3])
dlist[4] = int(dlist[4])
dlist[5] = dlist[2]+dlist[3]+dlist[4]
dlist[6] = dlist[5]/3
dlist2 = [str(i) for i in dlist]
print(dlist)

# 특정문자로 결합  - join
# 문자열리스트만 변경가능 join결합
# 문자열로 변환됨
d_str = ",".join(dlist2)
print(d_str)


# 5. count : 문자열 안에 해당문자가 몇개 있는지 확인
# 6. find : 문자열안에 해당문자가 위치 반환, 없으면 -1
# 7. index : 