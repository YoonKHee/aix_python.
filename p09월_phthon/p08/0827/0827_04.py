import random
#import datetime # 현재시간을 가져오는 클래스 선언 datetime 2번 사용해야함
# now = datetime.datetime.now()
# print(now)

# from datetime import datetime # datetime 1번 사용
# now = datetime.now()
# print(now)


# 현재시간
# now = datetime.datetime.now()
# print(now)


# print("전체:",now)        #전체시간
# print("년도:",now.year)   #년도
# print("월:",now.month)  #월
# print("일:",now.day)    #일
# print("시:",now.hour)   #시
# print("분:",now.minute) #분
# print("초:",now.second) #초


# format 함수 사용으로 지금 시간 나타내기

# print("{}년{}월{}일\t{}시{}분{}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

# print(f"{now.year}년{now.month}월{now.day}일\t{now.hour}시{now.minute}분{now.second}초")


# 1-6월 까지는 상반기
# 7-12월 까지는 하반기
# 8월
# 현재월을 datetime함수를 사용해서 검색한 다음 상반기,하반기인지 출력하시오

# 1. 날짜 함수 사용해서 월을 변수에 저장
# 2. 비교
# 3. 출력

from datetime import datetime
now = datetime.now()
a = now.month

if a>=7:
    print("{}월. 하반기".format(a))
else:
    print("{}월. 상반기".format(a))
