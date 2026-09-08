# import student as st
from student import Student
from students import Students
from stuFunc import*

# 잘 동작 되는지 확인용
# # st = Student(1,"홍길동",100,100,99)
# s = Student(1,"홍길동",100,100,99)
# print(s)

# stus = Students(s)
# stus.print()
# import stu_m as pm


readStu()# 파일불러오기
while True:
# 메인화면함수
    choice = main_screen()
# 1. 학생성적입력함수
    if choice==1:
        stu_input()
# 2. 학생성적출력함수
    elif choice==2:
        stu_output()
    elif choice==3:
        stu_update()
    elif choice==8:
        print("[ 등수처리 ]")
    elif choice==9:
        writeStu()
    else: 
        print("프로그램 종료")
        break

