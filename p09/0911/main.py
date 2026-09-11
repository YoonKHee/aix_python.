from stuFunc import*
from student import*
from students import*
stus = Students()


while True:
    choice = main()
    if choice==0:
        print("프로그램 종료.")
        break
    if choice==1:
        s_input()
    if choice==2:
        stus.print()
    if choice==3:
        s_update()
    if choice==9:
        save()