# format함수
# a = 10
# print("{}".format(a))
# print("{:10d}".format(a))
# print("{:010d}".format(a))
# print("{:d}".format(-3)) # 음수를 넣으면 음수가 나옴
# print("{:3,d}".format(123456789)) # 쉼표를 넣으면 1,000단위 표시   # 123,456,789
# print("{:.2f}".format(12.3456789)) # 소수점제한(2번째 자리에서 반올림해라)







# 이 두 개는 알아두면 좋음
#______________________________________________________


# ★★★ 문자인지 아닌지 확인 ★★★
# 이름을 입력을 받는데 영문이름
# name = input("이름: ")
# if name.isalpha():# 특수문자나 숫자인지 확인가능
#     print("문자 알파벳으로 되어 있습니다.")
# else: print("특수문자나 숫자 입력되었습니다.")
# print(name)


# num = input("숫자:")
# if num.isdigit():
#    num = int(num)
#    num += 100
#    print("입력숫자 :",num2)
# else: print(num)


# name = input("이름: ")
# while(True):
#     kor = input("국어: ")
#     if kor.isdigit():
#        kor = int(kor)
#        break
#     else: print("숫자가 아닙니다. 다시 입력해주세요.")    
# print(name,kor)

# #______________________________________________________



# while(True):
#     id = input("아이디: ") 
#     pw = input("패스워드: ")
#     if id=="aaa" and pw=="1111":
#         print("로그인 성공!")
#         break
#     else: print("아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인 해주세여.")

# print("메인페이지가 열립니다")





paper = "네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서\
        2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.\
        이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서\
        비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."



if "코치" in paper:
    print('o')
else:
    print("x")

# print(paper.find("홍수"))

# print(paper.rfind("홍수"))

# print(paper.count("홍수"))


### 홍수라는 글자가 어디어디에 있는지 위치점을 알고싶다

# result = paper.find("홍수")
# print(paper.find("홍수",5))

# split() 구분자로 분리
# srt1 = "1,홍길동,100,100,100"
# s = srt1.split(",")
# print(s)     # 리스트 - 문자열
# print(s[4])  # 타입:문자열


str1 = "1,홍길동,100,100,77"
# 번호,이름,국어,영어,수학,합계,평균을 출력하시오
s = str1.split(",")
# total = int(s[2])+int(s[3])+int(s[4])
# avg = total/3

s[2] = int(s[2])
s[3] = int(s[3])
s[4] = int(s[4])
s.append(s[2]+s[3]+s[4])
s.append(s[5]/3)
print("[학생성적프로그램]")
print("-"*75)
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*75)
# print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{total}\t{avg:.2f}")
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s)) # 구조분해할당 리스트를 분리해서 출력시켜준다 format(*) 이런 형식에서만 가능
print("-"*75)




