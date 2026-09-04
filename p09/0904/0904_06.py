# # r: 파일읽기, w:파일쓰기, a:파일쓴거 저장


# # fw = open("C:/aaa/abc.txt","w",encoding = "utf-8")
# # fw.close()

# with open("C:/aaa/abc.txt","a",encoding= "utf-8") as fw:
#     while True:
#         line = input("글입력:")
#         if line !="":
#             fw.writelines(line+"\n") # \r: 문장 끝으로 ,\n:문장 줄바꿈
#         else:
#             break

# print("파일이 저장됨.")