# 학생성적프로그램
#     학생입력
#     학생출력
#     학생성적수정
#     학생성적삭제
# 학생검색
# 프로그램종료

stu = []
while True:
    print("\t","학생성적프로그램","\t")
    print("\t","0. 프로그램 종료","\t")
    print("\t","1. 학생성적입력","\t")
    print("\t","2. 학생성적출력","\t")
    print("\t","3. 학생성적수정","\t")
    print("\t","4. 학생성적삭제","\t")
    print("\t","5. 학생검색","\t")
    print("-"*60)
    click = int(input("프로그램 번호입력:"))
    if click ==0:
        print("종료")
        break
    elif click==1:
        print("학생입력")
        while True:
            no = len(stu)+1
            print("자동번호",no)
            name = input("이름:")
            if name=="0":
                print("종료")
                break
            kor = int(input("국어점수:"))
            eng = int(input("영어점수:"))
            math = int(input("수학점수:"))
            total = kor+eng+math
            avg = total/3
            stu.append([no,name,kor,eng,math,total,avg])
            print("학생 성적이 입력되었습니다.")
        print("-"*60)
    elif click==2:
        print("학생성적출력")
        print("-"*60)
        print(f"입력된 학생수{len(stu)}:")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for i in stu:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*i))
    elif click==3:
        print("학생성적수정")
        stu[input("바꿀학생번호입력:"-1)][input("바꿀거 입력(번호:0, 이름:1, 국어:2, 영어:3, 수학:4, 합계:5, 평균:6):")] = input("바꿀값을 입력:")
    elif click==4:
        print("학생성적삭제")
    elif click==5:
        print("학생검색")
else:print("프로그램 종료")

