# 1. 번호, 이름, 국어, 영어, 수학
# 2. 합계, 평균
# 3. 성적출력하도록 구성하시오

# 입력 ->변수저장 ->DB저장
s =[]#리스트타입 - 추가 :append(젤 뒤에 추가), insert(사이에 추가) / 삭제 : pop,del,romove
no = (input("번호 입력:"))
name = (input("이름 입력:"))
kor = int(input("국어점수 입력:"))
eng = int(input("영어점수 입력:"))
math = int(input("수학점수 입력:"))
total = kor+eng+math
avg = total/3 #나눗셈을 하면 실수 타입이 됨.: float

print("[학생성적프로그램]")
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60) #문자를 곱하면 반복.
print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}")

#print("{}{}{}{}{}{}{:.2f}").format(no,name,kor,eng,math,total,avg) 2개의 포맷 숙지하기