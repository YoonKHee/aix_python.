from student import*
from students import*

s_no = 1
stus = Students()


def main(): #1 메인화면
    print("[ 학생성적프로그램 ]")
    print("0.프로그램종료")
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("3.학생성적수정")
    print("4.학생성적삭제")
    print("5.학생성적저장")
    choice = int(input("번호입력"))
    return choice



def s_input():#2 성적입력화면
    global s_no
    while True:
        print()
        print("학생성적입력")
        print("-"*60)
        no = s_no
        name = (input("이름(0.이전화면):"))
        if name=="0":
            break
        kor = int(input("국어:"))
        eng = int(input("영어:"))
        math = int(input("수학:"))
        stus.add(Student(no,name,kor,eng,math))
        print(f"{no}.{name}학생 성적이 저장되었습니다")
        print()
        s_no += 1

# 학생성적변경
def c_score(sub,score):
    print(f"{sub}점수 변경")
    print("현재점수:",score)
    return int(input("변경점수 :"))


# 학생성적수정
def s_update():
    print()
    print("[ 학생성적수정 ]")
    name = input("학생이름:")
    temp = 0
    for s in stus.slist:
        if s.name == name:
            temp = 1
            print(f"{name}학생이 검색되었습니다.")
            print(" 수정과목 ")
            print("1.국어 2.영어 3.수학")
            choice = int(input("바꿀과목 번호 입력:"))
            if choice==1:
                s.kor = c_score("국어",s.kor)
            elif choice==2:
                s.eng = c_score("영어",s.eng)
            elif choice==3:
                s.math = c_score("국어",s.math)
            s.s_total()
            s.s_avg()
            print("수정되었습니다")
            print()
    if temp ==0:
        print(f"{name}학생이 없습니다.")


# # 학생성적저장하기
# def writeStu():
#     print("학생성적저장")
#     global s_no
#     with open("C:\\Users\\admin\\Desktop\\Ai융복합 학원\\python\\aix_python.-main\\aix_python.-main\\p09\\stu.txt","w",encoding="utf-8") as f:
#         for s in stus.slist:
#             str = s.s_str()
#             f.write(str+"\n")
#         print("파일이 저장되었습니다")
#         print()


def stuWrite():
    global s_no
    with open("C:\\workspace\\Python\\aix_python\\2026\\new.txt","w",encoding="utf-8") as f:
        for s in stus.slist:
            str = s.s_str()
            f.write(str+"\n")
        print("파일저장 완료")
        print()


#학생성적불러오기
# def readStu():
#     global s_no
#     with open("C:\\Users\\admin\\Desktop\\Ai융복합 학원\\python\\aix_python.-main\\aix_python.-main\\p09\\stu.txt","r",encoding="utf-8") as f:
#         while True:
#             str = f.readline()
#             if str =="": break
#             stu = str.split(",")
#             for i,s in enumerate(stu):
#                 if 0<=i<=1:continue
#                 elif 2<=i<=5:stu[i] = int(s.strip())
#                 elif i==6: stu[i] = float(s.strip())
#                 elif i==7: stu[i] = int(s.strip())
#             stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4]))
#             s_no = len(stus.slist)+1

def stuRead():
    with open("C:\\workspace\\Python\\aix_python\\2026\\new.txt","r",encoding="utf-8") as f:
        global s_no
        while True:
            str = f.readline()
            if str == "": break
            stu = str.split(",")
            for i,s in enumerate(stu):
                if 0<=i<=1:continue
                elif 2<=i<=5 or i==7:
                    stu[i] = int(s.strip())
                elif i==6: 
                    stu [i] = float(s.strip())
            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4]))
            s_no = len(stus.slist) + 1

# 학생성적 삭제하기
def delStu():
    print("학생성적삭제")
    stus.print()
    bye = int(input("삭제학생 번호입력:"))
    for i,s in enumerate(stus.slist):
        if s.no ==bye:
            stus.slist.pop(i)
            print(f"{bye}번 학생이 삭제되었습니다.")   
            break
