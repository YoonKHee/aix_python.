
from student import*
from students import*
from func import*





while True:
    choice = main()
    if choice == 0:
        print("종료")
        break 
    elif choice ==1:
        s_input()

    elif choice ==2:
        print("출력")

    elif choice ==3:
        print("수정")

    elif choice ==9:
        print("저장")

    else: pass

















# stus = Students()

# s1 = Student(1,"홍길동",100,98,96)
# stus.add(s1)
# s2 = Student(2,"유관순",100,100,100)
# stus.add(s2)

# stus.print()
# stus = Students()
# student -> Student클래스
# 홍길동성적 = stus.add(s1)
# 유관순성적 = stus.add(s2)

















# stuList = []

# s1 = Student(1,"홍길동",100,98,96)
# stuList.append(s1)
# s2 = Student(2,"유관순",100,100,100)
# stuList.append(s2)

# for i in stuList:
    # print(i)


# student -> Student 클래스
# 홍길동 성적 -> stuList.append(s1)
# 유관순 성적 -> stuList.append(s2)

# 학생성적출력
# for 문 사용해서 출력