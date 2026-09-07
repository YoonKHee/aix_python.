m_str = '"서울특별시  (1100000000)","9,330,658","4,482,949","          2.08","4,504,432","4,826,226","          0.93"'

list = m_str.split('","')
for i,t in enumerate(list):
    t = t.replace('"','')
    t = t.replace(',','')
    t = t.strip()
    if t.isdigit():
        list[i] = float(t)
    print(type(t))
print(list)
#---------------
# 서울 전체 인구에서 남성비율은 몇 퍼센트 인가?
print("서울 총인구 남성비율:{:.2f}%".format(list[4]/list[1]))












# # common폴더 안에 stu.txt로 저장하시오.
# #1
# # 홍길동
# #...
# with open("common/stu.txt","w",encoding="utf-8") as f:
#     allStr = ""
#     no = 0
#     while True:
#         str = input("입력:")
#         if no ==0: 
#             allStr = str
#             no += 1
#             continue
#         else:
#             if str =="":
#                 f.write(allStr+'\n')
#                 break
#             allStr += ','+str
#         no += 1
#         print(allStr)
# print("파일저장되었습니다.")