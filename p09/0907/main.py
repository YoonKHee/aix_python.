# 학생성적프로그램
# 학생성적입력
# 학생성적출력
# 학생정보수정
# 성적파일저장
from func1 import*


read_stu()
while True:
    choice = main()
    if choice == 0: break
    elif choice == 1:
        stu_input()
    elif choice == 2:
        stu_output()
    elif choice == 3:
        pass
    elif choice == 9:
        write_stu()
    else: pass
