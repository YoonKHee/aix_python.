from student import Student
from students import Students



s_no = 1
stus = Students() # stus = 참조변수 , Students = 객체선언


def main():
    print("[ 학생성적프로그램 ]")
    print("0.종료")
    print("1.입력")
    print("2.출력")
    print("3.수정")
    print("9.저장")
    choice = int(input("번호입력:"))
    return choice


def s_input():
    while True:
        global s_no
        print("학생정보입력")
        no = s_no
        name = input("이름입력:")
        if name == "0":
            break
        kor = int(input("국어:"))
        eng = int(input("영어:"))
        math = int(input("수학:"))
        stus.add(Student(no,name,kor,eng,math))
        print(f"{s_no}.{name}학생 성적이 저장되었습니다.")
        print()
        s_no += 1


def s_output():
    while True:
        stus.print()