# 파일 복사하기
import os

rf = open("C:\\aaa\\4.jpg","rb")
wf = open("C:/aaa2/5.jpg","wb")

while True:
    fdata = rf.read(1)
    if not fdata:break
    wf.write(fdata)

rf.close()
wf.close()
print("이미지 파일이 복사되었습니다.")