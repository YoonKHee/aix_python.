from student import*
from students import*
stus = Students()
s_no = 1

# 메인화면함수
def main():
    print("[ 학생성적프로그램] ")
    print("1.성적입력.")
    print("2.성적출력.")
    print("3.성적수정.")
    print("9.성적파일저장.")
    print("0.프로그램종료.")
    print("-"*60)
    choice = int(input("원하는 번호 입력:"))
    return choice

# 학생성적입력함수
def s_input():
    global s_no
    while True:
        print("-"*60)
        print("학생성적입력:")
        print()
        no = s_no
        name = input("이름:(0.이전화면)")
        if name == "0": break
        kor = int(input("국어점수:"))
        eng = int(input("영어점수:"))
        math = int(input("수학점수:"))
        stus.add(Student(no,name,kor,eng,math))
        print(f"{name}학생이 저장되었습니다.")
        s_no += 1


# 성적출력함수
def s_update():
    print("학생성적수정")
    print()
    name = input("수정할 학생이름 검색:")
    temp = 0
    for s in stus.slist:
        if s.name == name:
            print(f"{name}학생이 검색되었습니다.")
            print("수정할 과목 번호 선택해주세요")
            choice = int(input("1.국어 2.영어 3.수학"))
            if choice == 1:
                s.kor = c_score("국어",s.kor)
            elif choice==2:
                s.eng = c_score("영어",s.eng)
            elif choice==3:
                s.math = c_score("수학",s.math)
            s.s_total()
            s.s_avg()
            print(f"{name}학생 성적이 수정되었습니다")
    if temp == 1:
        print(f"{name}학생이 없습니다.")



def c_score(sub,score):
    print(f"{sub}점수 변경")
    print("현재점수:",score)
    return int(input("변경점수 :"))



#성적파일저장
def save():
    with open("C:\\workspace\\Python\\aix_python\\new.txt","r",encoding="utf-8")as f:
        for s in stus.slist:
            str= s.s_str()
            f.write(str+"\n")
        print("저장되었습니다")
        print()
