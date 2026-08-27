# 조건문 안에 조건문
# if문 안에 if문을 넣을 수 있다. 허나 보통 if는 3번이상 쓰지 않는것을 권장함.
# a = 105
# if a>50:
#     if a<100:
#         print("50보다 크고, 100보다 작은수")
#     else:
#         print("50보다 크고, 100보다 큰수")
# else:
#     print("50보다 작은수")#


# 조건물을 여러개 사용할때는 elif를 사용
# score = 65
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")  
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")



# import random
# random_no = random.randint(-10,10)
# print("랜덤숫자 :",random_no)
# if random_no<0:
#     print("음수")
# elif random_no>0:
#     print("양수")
# else:
#     print("0이다")


# import random
#0-100점 랜덤숫자 생성
#60점 이상 합격
#50~59점 재시험
#0~49 불합격

# random_score = random.randint(0,100)
# print("내 점수:",random_score)
# if random_score>=60:
#     print("합격")
# elif random_score>=50: #위에 프린트에서 60점 이상은 날라가서 59이하는 안써도됨. 
#    # if 59>=score>=50 이렇게 사용가능
#     print("재시험")
# else:
#     print("불합격")


# 랜덤점수를 생성해서
#90점 이상은A 80이상은B, 70C 60D 그외F
# 랜덤점수도 출력
# if : 조건문
# if 1개
# if else 2개
# if elif else 3개
# if elif elif else 4개

# if 조건문:         #들여쓰기 해야한다
#     들여쓰기 되어야함
# elif 조건문:
#     들여쓰기


# if 10>5:
#     pass # 출력이나 기타 프로그램이 없을시 pass
#          # 빈공백이면 에러남


# if 10>5: pass        # 한줄로 쓰기 가능
# if 10>5: print("참") 
# if 10>5:              
#     print("참")

# if 10>5:       #명령어가 두줄 이상이면 다음줄에 넣어야함
#     print("참")
#     print("거짓")

# import random
# score = random.randint(0,100)
# print("내 점수:",score)
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")



# if score>=90:
#     if score>=98:
#         print("A+")
#     elif score>=93:
#         print("A")
#     else:
#          print("A-")
# elif score>=80:
#     if score>=88:
#         print("B+")
#     elif score>=83:
#         print("B")
#     else:
#          print("B-")
# elif score>=70:
#     if score>=78:
#         print("C+")
#     elif score>=73:
#         print("C")
#     else:
#         print("C-")
# elif score>=60:
#     if 68>score>=68:
#             print("D+")
#     elif score>=63:
#             print("D")
#     else:
#          print("D-")
# else:
#     print("F")



# 날씨함수를 사용하려면
import datetime
now = datetime.datetime.now()

# 해당월에 따라 봄, 여름, 가ㄴ을, 겨울이라고 출력
# 겨울 12,1,2 봄 ,3,4,5 여름 6,7,8 가을 9,10,11
# 비교문을 사용
# 해당월 계절 출력
# now.month

# a = now.month

# a = int(input("월을 입력:"))
# if 12==a or a<3:
#     print("겨울")
# elif 6>a>2:
#     print("봄")
# elif 9>a>5:
#     print("여름")
# else:
#     print("가을")


# score = 65
# dcore 60점 이상이면합격 그외 불합
# if score >=60: print("합격")
# else: print("불합격")

#if문 축약
score = 65
result = "합격" if score>=60 else "불합격"
print(result)