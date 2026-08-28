# paper = """네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 
# 2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
# 이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서 
# 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다.
# """

# print(paper)
# print(len(paper))






# 문자열 함수
# split, strip, replace, find, rfind
# upper - 영문자를 모두 대문자 출력, lower - 모두 소문자 출력

# # split : 입력문자 기준으로 분리해줌
# str1 = "1,hgd,100,100,100,300,100" #문자열 타입
# s = str1.split(",") # split 특정문자를 기준으로 분리해줌.
# print(s)
# print(s[1])

# str2 = "2026-08-28"
# s2 = str2.split("-")
# print(s2)
# print(s2[2])

# str3 = "안녕 반가워 다음에 봐"
# s3 = str3.split(" ")
# print(s3)
# print(s3[2])


# str4 = "EDMS,307-2E-PS-W-611-W008,VF5770"
# s4 = str4.split(",")
# print(s4)
# print(s4[2])


# # strip: 공백제거
# aaa1 = "       안녕하세요      "
# print(aaa1)
# print(aaa1.strip())


# aaa2 = "    안녕   하세요      "
# print(aaa2.strip())


# # replace - 치환함 (문자를 다른 문자로 대체)
# aaa3 = "aaavvggeedd"
# aaa4 = aaa3.replace("a","K")
# print(aaa4)


# aaa2 = "    안녕   하세요      "
# aaa5 = aaa2.replace(" ","") #공백을 빈공백으로 치환
# print(aaa5)

# # find : 검색함수(몇번 인데스에 위치해 있는지.)있으면 위치를 알려주고 없으면 -1
# bb = "abcdefcbsdaceghi"
# print(bb.find("e"))

# print(bb.rfind("e")) # rfind는 뒤에서 부터 검색



# upper - 모두 대문자 변경, lower - 모두 소문자 변경
cc = "aabbccddee"
cd = "AABBCCDDEE"
print(cc.upper())
print(cd.lower())