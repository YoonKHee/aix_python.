# import datetime
# now = datetime.datetime.now()
# print(now)


# # format
# # 123 -> 5자리 빈 공백 0으로 채워서 출력하시오
# print("{:05,d}".format(123456)) # :05d 사이에 쉼표를 넣으면 :05,d, 1000단위 쉼표가 생김. 123,456
# print("{:05d}".format(8))


#월을 출력하는데, 1,2,3,....9월, 01,02...09,10 이렇게 두자리 수로 나타내고 싶을때
import datetime
now = datetime.datetime.now()
# print("{:02d}월".format(now.month))
# print("{:02d}분".format(now.minute))
# print("{:02d}초".format(now.second))


# print(now)
f_date = now.strftime("%Y/%m/%d - %H:%M:%S") # format문보다 단순함 복잡하지 않다.
print(f_date)