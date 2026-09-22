# list로 학생 성적표 만들기

s = [0,0,0,0,0,0,0]
s[0] = input("번호: ")
s[1] = input("이름: ")
s[2] = int(input("국어: "))
s[3] = int(input("영어: "))
s[4] = int(input("수학: "))
s[5] = s[2]+s[3]+s[4]
s[6] = s[5]/3

print("-"*70)
print("학생성적표")
print("-"*70)
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*70)
print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}")