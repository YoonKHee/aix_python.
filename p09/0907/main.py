# 학생성적프로그램
# 학생성적입력
# 학생성적출력
# 학생정보수정
# 성적파일저장
from func1 import*

stuList = []
title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
s_title = ["no","name","kor","eng","math","total","avg","rank"]
stuNum = 1 # 전역변수

def write_stu():
    with open("C:/aaa/stu.txt",'w',encoding='utf-8') as f:
        for i in stuList:
            str = f"{i['no']}{i['name']}{i['kor']}{i['eng']}{i['math']}{i['total']}{i['avg']}{i['rank']}"
            f.write(str+"\n")
    print("저장되었습니다.")
    print()




# 메인화면
def main():
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("0. 프로그램종료.")
    print("1. 성적입력.")
    print("2. 성적출력.")
    print("3. 성적수정.")
    print("9. 성적파일저장.")
    print("-"*60)
    print()
    choice = int(input("번호입력:"))
    return choice

# 학생입력프로그램
def stu_input():
    global stuNo
    print()
    print("[ 학생입력프로그램 ]")
    print("-"*60)
    while True:
        no = stuNo
        name = input("이름입력(0.이전화면):")
        if name=="0": break
        kor = int(input("국어점수:"))
        eng = int(input("영어점수:"))
        math = int(input("수학점수:"))
        total = kor + eng + math
        avg = total/3
        rank = 0
        stuList.append({'no':no,'name':name,
                        'kor':kor,'eng':eng,'math':math,
                        'total':total,'avg':avg,'rank':rank})
        print(f"{no}.{name}학생이 저장되었습니다.")
        stuNo += 1
# 학생출력프로그램
def stu_output():
    print()
    print("[ 학생출력프로그램 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in stuList:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()

# 학생성적불러오기
def read_stu():
    global stuNo
    with open("C:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            str = f.readline()
            if str =="":break
            stu = str.split(",")
            for i,s in enumerate(stu):
                if i==0 or i==1:continue
                elif 2<=i<=5:
                    stu[i] = int(s.strip())
                elif i==6:
                    stu[i] = float(s.strip())
                elif i==7:
                    stu[i] = int(s.strip())
            stuList.append(dict(zip(s_title,stu)))
            stuNo = len(stuList)+1
        




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