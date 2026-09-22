import os
# r-읽기, w-쓰기, a-이어쓰기
# 없는 폴더에 파일저장시 에러
fname = input("저장할 파일이름을 입력하세요(파일명)>>")


if not os.path.exists("common"):
    os.makedirs("common") # 폴더를 생성해줌.
with open("common/"+fname,"a",encoding="utf-8") as f:
    while True:
        outStr = input("입력:")
        if outStr == "":break
        f.write(outStr+"\n")

print("파일내용이 저장되었습니다.")









# with open("C:\\aaa\\abc.txt","r", encoding="utf-8") as f:
#     while True:
#         str = f.readline()
#         if str =="": break
#         print(str,end="")




# sum = 0
# with open("C:\\aaa\\aaa.txt","r", encoding="utf-8") as f:
#     while True:
#         str = f.readline()
#         if str =="":break
#         if str.strip().isdigit():
#             str = int(str)
#             sum += str
#         print(str,end="")

# print("합계:",sum)
        
        





# stu.txt 출력
# stuList = []
# with open("C:\\aaa\\stu.txt","r",encoding="utf-8") as f:
#     while True:
#         str = f.readline()
#         if str =="":break
#         stu = str.split(",")#, 기준으로 생성
#         for i,s in enumerate(stu):
#             if i==0 or i==1:continue
#             elif 2<=i<=5:
#                 stu[i] = int(s.strip())
#             elif i==6:
#                 stu[i] = float(s.strip()) #/n 제거해야함.
#         stuList.append(stu)
#     print("파일 읽어오기 완료")
# print(stuList)



# # with 파일 읽어오기 - close 생략가능 
# 한글은 꼭 encoding = "utf-8"
# with open("C:\\aaa\\abc.txt","r", encoding = "utf-8") as f:
#     while True:
#         str = f.readline()
#         if str=="":break
#         print(str,end="")

# open() 파일 읽어오기
# f = open("C:\\aaa\\abc.txt","r", encoding = "utf-8")

# while True:
#     str = f.readline()
#     if str == "": break
#     print(str,end="")
# f.close()

# print("프로그램 종료")
#
