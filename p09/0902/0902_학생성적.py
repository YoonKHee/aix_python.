# 학생성적
stu = [
    # {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":},
    # {},
    # {}
]


# 화면출력
# 1. 성적출력
# 2. 성적출력
c_no = 0 # 학생번호로 사용
while True:
    print("[ 학생성적프로그램 ]")
    print("-"*60)
    print("1. 학생성적입력:")
    print("2. 학생성적출력:")
    print("-"*60)
    choice = int(input("원하는 번호 입력:"))
    # 학생성적입력부분
    if choice == 1:
        while True:
            print()
            print("[ 학생성적입력 ]")
            no = c_no
            name = input("이름:")
            if name =="0":
                break
            kor = int(input("국어점수:"))
            eng = int(input("영어어점수:"))
            math = int(input("수학점수:"))
            total = kor+eng+math
            avg = total/3
            stu.append({"no":no,"name":name,"kor":kor,"eng":eng\
                        ,"math":math,"total":total,"avg":avg})
            print(name,"학생성적저장")
            c_no += 1 # 자동번호증가
            print()


    # 학생성적 출력부분
    elif choice ==2:
        print()
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("-"*60)
        for s in stu:
            print(f"{s['no']+1}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
        