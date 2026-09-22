def main():
    print("학생성적프로그램")
    print("1.학생입력")
    print("2.학생출력")
    print("3.학생수정")
    print("4.학생저장")
    print("0.프로그램 종료")
    choice= int(input("번호 :"))
    return choice


while True:
    choice = main()
    if choice ==0:
        print("프로그램종료")
        break
    elif choice==1:
        print()
        print("학생입력")
        print("-"*60)
    elif choice==2:
        print()
        print("학생출력")
        print("-"*60)
    elif choice==3:
        print()
        print("학생수정")
        print("-"*60)
    elif choice==4:
        print()
        print("학생저장")
        print("-"*60)

