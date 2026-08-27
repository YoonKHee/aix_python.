# 학생 2명의 성적을 입력받아 출력하시오.
# 번호,이름,국어,영어,수학 점수를 입력받아
# 번호 이름 국어 영어 수학 합계 평균을 출력하시오

# 이런 순서가 머리속에 정리 되어야함.
# 성적입력
# 성적처리 수식
# 성적출력


# 성적입력
# 나
no = input("번호를 입력하시오.")
name = input("이름을 입력하세요.")
kor = int(input("국어점수를 입력하시오.")) # 한줄복사 shift alt 방향키
eng = int(input("영어점수를 입력하시오."))
math = int(input("수학점수를 입력하시오."))

# 성적처리 수식
sum = kor+eng+math
avg = sum/3

# 성적입력
# 너
no1 = input("번호를 입력하시오.")
name1 = input("이름을 입력하세요.")
kor1 = int(input("국어점수를 입력하시오."))
eng1 = int(input("영어점수를 입력하시오."))
math1 = int(input("수학점수를 입력하시오."))

# 성적처리 수식
sum1 = kor1+eng1+math1
avg1 = sum1/3

# 성적출력
print("-"*110)
print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t")
print("-"*110)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}"\
      .format(no,name,kor,eng,math,sum,avg))
print("-"*110)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}"\
      .format(no1,name1,kor1,eng1,math1,sum1,avg1))
print("-"*110)



