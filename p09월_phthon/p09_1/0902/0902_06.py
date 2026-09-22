def main_print():
    print("[학생성적프로그램]")
    print("0. 종료")
    print("1. 학생입력:")
    print("2. 학생출력:")
    print("3. 학생성적수정:")
    print("4. 학생성적삭제:")
    print("5. 학생검색:")
    print("0. 프로그램종료:")
    print("-"*40)

def stu_input(): # 학생입력함수
        print("[학생성적입력]")
        while True:
            no = len(stu_list)+1
            print("자동번호",no)
            # no = input("번호:")
            name = input("이름(종료하려면 0):")
            if name=="0":break
            kor = int(input("국어점수:"))
            eng = int(input("영어점수:"))
            math = int(input("수학점수:"))
            total = kor+eng+math
            avg = total/3
            stu_list.append([no,name,kor,eng,math,total,avg])
            print("학생성적이 입력되었습니다")
            print()


stu_list = []
while True:
    main_print()# 함수호출
    print()
    choice = int(input("원하는 번호 입력>>"))
    if choice == 1:
        stu_input()
    elif choice == 2:
        print(["학생성적출력"])
        print("입력된 학생 성적:",len(stu_list))
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))
    elif choice == 3:
        print("[학생성적수정]")
        i = int(input("학생 번호:"))
        j = int(input("1이름2국어3영어4수학5합계6평균:"))
        stu_list[i-1][j] = input("바꿀내용입력")
    elif choice == 4:
        print("[학생성적삭제]")
    elif choice == 5:
        print("[학생검색]")
    elif choice ==0:
        print(["프로그램 종료"])
        break
    else:
        print("등록된 숫자만 입력하세요.")